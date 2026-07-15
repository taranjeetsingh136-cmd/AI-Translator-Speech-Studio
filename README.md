# AI Translator and Speech Studio

A Streamlit capstone project for multilingual text translation and speech generation. The application accepts typed text or uploaded PDF, TXT, CSV, XLSX, and XLS files, translates the content using Google Gemini API, converts the translated output into speech using gTTS, and allows users to download both translated text and MP3 audio.

## Project Overview

**AI Translator and Speech Studio** is a Streamlit-based capstone application that performs text translation with Gemini API and speech generation with gTTS while supporting both manual text input and multiple uploaded document formats.

## Features

- Streamlit-based user interface
- Manual text input
- PDF, TXT, CSV, XLSX, and XLS upload support
- Gemini API-based translation
- gTTS-based text-to-speech generation
- MP3 playback and download
- Translated text download
- User-friendly validations and error messages
- Deployment-ready project structure
- Documentation and test case support

## Folder Structure

```text
AI Translator and Speech Studio-CapStone Project
├── app.py
├── requirements.txt
├── README.md
├── documentation.md
├── test_cases.md
├── .env.example
├── .gitignore
├── .streamlit/
│   └── config.toml
├── .github/
│   └── repo_description.txt
├── utils/
│   ├── file_handlers.py
│   └── languages.py
└── sample_data/
    ├── sample_input.txt
    ├── sample_table.csv
    └── sample_excel.xlsx
```

## Local Run Guide

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
notepad .env
streamlit run app.py
```

### Windows CMD

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env
streamlit run app.py
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
streamlit run app.py
```

## Run Command

```bash
streamlit run app.py
```

## Deployment

This application is deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the complete project to a GitHub repository.
2. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click **New app** and select the GitHub repository.
4. Set the main file path to `app.py`.
5. In **Advanced settings** or **Secrets**, add the required secret:
   - `GEMINI_API_KEY`
6. Deploy the application.
7. Test the following in the deployed app:
   - Manual text translation
   - File upload translation
   - Audio generation and download

## Notes

- For local execution, use the `.env` file.
- For deployed execution, use Streamlit secrets.
- Do not commit your real API key to GitHub.