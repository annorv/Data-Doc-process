import streamlit as st

def inject_custom_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def navbar():
    with st.sidebar:
        inject_custom_css("static/style.css")

        # Links to different pages
        st.write("## Navigation")
        