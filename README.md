# AI Translator and Speech Studio

A Streamlit capstone project for multilingual text translation and speech generation.. The application accepts typed text or uploaded PDF/TXT/CSV/Excel files, translates the content using Google Gemini API, converts the translated output into speech using gTTS, and allows users to download both translated text and MP3 audio.

## GitHub Repository Description
**AI Translator and Speech Studio** is a Streamlit-based capstone app that performs text translation with Gemini API and speech generation with gTTS, while supporting text input and multiple uploaded document formats.

## Features
- Streamlit UI
- Manual text input
- PDF, TXT, CSV, XLSX, and XLS upload support
- Gemini API based translation
- gTTS based text-to-speech generation
- MP3 playback and download
- Translated text download
- User-friendly validations and error messages
- Sample data for testing
- GitHub-ready documentation and submission notes

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

## How to compile/run
 Use the following command:

```bash
streamlit run app.py
```



## Deployment

This application is deployed using **Streamlit Community Cloud**.

### Deployment steps
1. Push the complete project to a GitHub repository.
2. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click **New app** and select the GitHub repository.
4. Set the main file path to `app.py`.
5. In **Advanced settings** or **Secrets**, add the required configuration values:
   - `GEMINI_API_KEY`
   - `GEMINI_MODEL="gemini-3.5-flash"`
6. Deploy the application and test the following:
   - manual text translation
   - file upload translation
   - audio generation and download


