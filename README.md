# Data & Document Processing App

## Description

This application is designed to help users process and analyze data from CSV files and PDF documents. The main features include:

- **Upload and Visualise CSV Files**: Users can upload CSV files, view their contents, and generate line charts. Customizations for charts are available, including selecting columns for X and Y axes.
- **Upload and Summarise PDF Files**: Users can extract and view text from PDF files and generate summaries of the extracted text.

Feel free to use the sidebar for navigation and explore different functionalities.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd your-repository
    ```

3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:

    - **On Windows**:
      ```bash
      .\venv\Scripts\activate
      ```

    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

- **Upload CSV**:
  - Go to the "Upload CSV" page in the sidebar.
  - Choose a CSV file to upload.
  - View the data and generate a default line chart.
  - Customise the chart by selecting columns for X and Y axes.
  - Save the customised chart as a PNG file.

- **Upload PDF**:
  - Go to the "Upload PDF" page in the sidebar.
  - Choose a PDF file to upload.
  - View the extracted text.
  - Generate and view a summary of the text.
  - Download the extracted text and summary as text files.

## File Structure

- `app.py`: Main application script.
- `navbar.py`: Contains the sidebar navigation code.
- `static/style.css`: Custom CSS for styling.
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**.
2. **Create a New Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make Your Changes**.
4. **Commit Your Changes**:
    ```bash
    git commit -m "Add your message here"
    ```
5. **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Create a Pull Request**.

Please make sure to follow the coding standards and include tests for any new features.

