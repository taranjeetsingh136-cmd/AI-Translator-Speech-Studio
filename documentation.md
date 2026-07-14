# Documentation - AI Translator and Speech Studio

## Cover Information
- Project Name: AI Translator and Speech Studio
- Academic Context: Generative AI and ML Capstone Project
- Platform: Streamlit
- Translation Engine: Google Gemini API
- Text-to-Speech Engine: gTTS

## Problem Statement
The objective of this project is to build a user-friendly web application that allows users to translate text into multiple languages and convert the translated text into downloadable speech output. The system should support direct input and uploaded files in PDF, TXT, CSV, XLSX, and XLS formats.

## Objectives
- Build a Streamlit web application
- Support multiple document input formats
- Translate using Gemini API
- Convert translated text into speech using gTTS
- Provide downloadable MP3 output
- Include documentation, testing, and deployment readiness

## Architecture Flow
1. User enters text or uploads a file.
2. File content is extracted using file processing helpers.
3. User selects a target language.
4. Gemini API translates the input text.
5. gTTS converts translated text into speech.
6. Application displays translated text and downloadable MP3 output.

## Files Included
- `app.py` - main Streamlit application
- `utils/file_handlers.py` - file extraction helpers
- `utils/languages.py` - language mappings
- `requirements.txt` - dependencies
- `README.md` - setup and usage guide
- `test_cases.md` - validation scenarios
- `.env.example` - environment variable template
- `.streamlit/config.toml` - UI theme settings
- `.github/repo_description.txt` - GitHub repository summary

## Setup and Usage
1. Install Python.
2. Create virtual environment.
3. Install requirements.
4. Configure `.env` with Gemini API key and pick Gemini model as 3.5
5. Run `streamlit run app.py`.
6. Test both manual and uploaded input.

## Limitations
- OCR is not included for scanned PDFs.
- Internet is required for Gemini API and gTTS.
- Very large documents may result in slower processing.
- Output quality depends on extracted source text quality.

## Challenges Faced
- Handling multiple file formats cleanly
- Providing a simple but polished UI
- Keeping the academic codebase straightforward
- Creating clear guidance for GitHub and Edureka submission

## Future Improvements
- Add OCR for scanned files
- Add language auto-detection
- Add translation history
- Add unit tests and CI pipeline
- Add Docker support

## Deployment

The final application is deployment-ready and can be hosted using Streamlit Community Cloud.

### Deployment platform
Streamlit Community Cloud was selected as the preferred deployment option because the project is built using Streamlit and can be hosted directly from a GitHub repository.

### Deployment procedure
1. Upload the final project code to GitHub.
2. Open Streamlit Community Cloud and create a new app.
3. Connect the GitHub repository containing the project.
4. Select `app.py` as the entry file.
5. Configure the required secrets:
   - `GEMINI_API_KEY`
   - `GEMINI_MODEL = "gemini-3.5-flash"`
6. Launch the application and verify translation, file upload, and speech generation features.

### Deployment outcome
The project satisfies the deployment requirement by being ready for public hosting through Streamlit Community Cloud and by supporting secure configuration of runtime secrets.
