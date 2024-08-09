import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import fitz  # pymupdf
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from heapq import nlargest
from navbar import navbar
import io

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load CSS and Navbar
navbar()

# Sidebar for navigation
page = st.sidebar.radio("Go to", ["Home", "Upload CSV", "Upload PDF"])

if page == "Home":
    st.title("Welcome to the Data & Document Processing App")

    st.write("""
    This app allows you to:
    
    - **Upload and Visualise CSV Files**: 
      - Upload a CSV file and view its contents.
      - See a default line chart of all columns.
      - Customise your chart by selecting columns for X and Y axes.
      - Save your customised charts.
      - As an example CSV file, we have the daily-bike-share.csv file to experiment with.
      
    - **Upload and Summarise PDF Files**:
      - Extract and view text from PDF files.
      - Generate a summary of the text.
      - As an example CSV file, we have the Making-Laws.pdf file to experiment with.
             

    Feel free to use the sidebar to navigate through the different features.
    """)

elif page == "Upload CSV":
    st.title("Upload CSV Files")

    st.header("This page allows you to upload a CSV file of your choice")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("DataFrame:")
        st.write(data)

        st.header("Data Visualisation")
        
        # Display default chart
        st.write("Here's a simple line chart of the data:")
        fig_default, ax_default = plt.subplots()
        data.plot(ax=ax_default)
        st.pyplot(fig_default)

        # Parameter Selection for custom chart
        st.subheader("Customise your chart")
        columns = data.columns.tolist()
        x_axis = st.selectbox("Select X-axis column", columns)
        y_axis = st.selectbox("Select Y-axis column", columns)

        if x_axis and y_axis:
            st.write(f"Line chart of {y_axis} vs {x_axis}")

            fig_custom, ax_custom = plt.subplots()
            data.plot(x=x_axis, y=y_axis, ax=ax_custom)
            st.pyplot(fig_custom)

            # Button to save the customised figure
            if st.button('Save Chart as PNG'):
                buffer = io.BytesIO()
                fig_custom.savefig(buffer, format="png")  # Save the customised chart
                buffer.seek(0)
                st.download_button(label="Download Chart", data=buffer, file_name="chart.png", mime="image/png")

elif page == "Upload PDF":
    st.title("Upload PDF Files")

    st.header("This page allows you to upload a PDF file of your choice")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    if uploaded_file is not None:
        # Extract text from PDF
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        with st.expander("View Extracted Text"):
            st.write(text)

        # Summarise the text
        def summarise_text(text, num_sentences=5):
            sentences = sent_tokenize(text)
            if len(sentences) < num_sentences:
                return text
            
            stop_words = set(stopwords.words('english'))
            word_frequencies = {}
            for word in word_tokenize(text):
                if word.lower() not in stop_words:
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

            max_frequency = max(word_frequencies.values())
            for word in word_frequencies.keys():
                word_frequencies[word] = word_frequencies[word] / max_frequency

            sentence_scores = {}
            for sent in sentences:
                for word in word_tokenize(sent.lower()):
                    if word in word_frequencies:
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores:
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]

            summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
            summary = ' '.join(summary_sentences)
            return summary

        summary = summarise_text(text, num_sentences=5)

        with st.expander("View Summary"):
            st.write(summary)

        # Download options
        if st.button('Download Extracted Text'):
            st.download_button("Download Text", text, file_name="extracted_text.txt")

        if st.button('Download Summary'):
            st.download_button("Download Summary", summary, file_name="summary.txt")
