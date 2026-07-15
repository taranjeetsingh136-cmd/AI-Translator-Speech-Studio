# Documentation - AI Translator and Speech Studio

## Cover Information

- Project Name: AI Translator and Speech Studio
- Academic Context: Generative AI and ML Capstone Project
- Platform: Streamlit
- Translation Engine: Google Gemini API
- Text-to-Speech Engine: gTTS

## Problem Statement

The objective of this project is to build a user-friendly web application that allows users to translate text into multiple languages and convert the translated text into downloadable speech output. The system supports both direct text input and uploaded files in PDF, TXT, CSV, XLSX, and XLS formats.

## Objectives

- Build a Streamlit web application
- Support multiple document input formats
- Translate content using Gemini API
- Convert translated text into speech using gTTS
- Provide downloadable MP3 output
- Include documentation, testing, and deployment readiness

## Architecture Flow

1. The user enters text manually or uploads a supported file.
2. The application extracts content using file handling helpers.
3. The user selects a target language from the dropdown.
4. Google Gemini API translates the input text.
5. gTTS converts the translated text into speech.
6. The application displays the translated text and provides downloadable MP3 output.

## Files Included

- `app.py` - Main Streamlit application
- `utils/file_handlers.py` - File extraction helpers
- `utils/languages.py` - Language mappings
- `requirements.txt` - Dependency list
- `README.md` - Setup and usage guide
- `test_cases.md` - Functional validation scenarios
- `.env.example` - Local environment template
- `.streamlit/config.toml` - Streamlit UI theme settings
- `.github/repo_description.txt` - GitHub repository summary

## Setup and Usage

1. Install Python on the local machine.
2. Create a virtual environment.
3. Install all required dependencies from `requirements.txt`.
4. Configure the Gemini API key in the local `.env` file for local use.
5. Run the application using `streamlit run app.py`.
6. For cloud deployment, configure the API key in Streamlit secrets.
7. Test both manual input and uploaded file workflows.

## Limitations

- OCR is not included for scanned PDF files.
- Internet access is required for Gemini API and gTTS.
- Very large documents may take longer to process.
- Output quality depends on the quality of extracted source text.

## Challenges Faced

- Handling multiple file formats in a clean and user-friendly way
- Designing a simple but polished Streamlit interface
- Keeping the project readable and suitable for academic evaluation
- Preparing documentation, testing notes, and deployment guidance for submission

## Future Improvements

- Add OCR support for scanned files
- Add automatic language detection
- Add translation history
- Add unit tests and CI/CD workflow
- Add Docker-based deployment support

## Deployment

The final application is deployed and is hosted using Streamlit Community Cloud.

### Deployment Platform

Streamlit Community Cloud was selected because the project is built with Streamlit and can be deployed directly from a GitHub repository.

### Deployment Procedure

1. Upload the final project code to GitHub.
2. Open Streamlit Community Cloud and create a new app.
3. Connect the GitHub repository containing the project.
4. Select `app.py` as the entry file.
5. Configure the required secret:
   - `GEMINI_API_KEY`
6. Launch the application.
7. Verify translation, file upload, speech generation, and download features.

### Deployment Outcome

The project satisfies the deployment requirement by supporting public hosting through Streamlit Community Cloud and secure runtime secret management.
