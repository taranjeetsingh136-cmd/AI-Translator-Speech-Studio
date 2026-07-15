import os
import tempfile
from datetime import datetime
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS
from google import genai

from utils.file_handlers import extract_text_from_uploaded_file
from utils.languages import LANGUAGE_OPTIONS, get_language_code

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)

st.set_page_config(
    page_title="AI Translator and Speech Studio",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
.hero-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: white;
    padding: 1.4rem 1.6rem;
    border-radius: 18px;
    margin-bottom: 1rem;
}
.info-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 1rem;
    border-radius: 16px;
    min-height: 120px;
}
.caption-small {font-size: 0.9rem; color: #475569;}
.success-banner {
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    padding: 0.8rem 1rem;
    border-radius: 12px;
    margin-top: 0.8rem;
}
.code-note {
    background: #111827;
    color: #f9fafb;
    padding: 0.75rem 1rem;
    border-radius: 12px;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        return None, "GEMINI_API_KEY is missing. Create a .env file and add your API key before translation."
    try:
        return genai.Client(api_key=api_key), None
    except Exception as exc:
        return None, f"Unable to initialize Gemini client: {exc}"


@st.cache_data(show_spinner=False)
def build_translation_prompt(input_text: str, target_language: str) -> str:
    return (
        f"Translate the following text into {target_language}. "
        "Preserve meaning, tone, and formatting as much as possible. "
        "Return only the translated text.\n\n"
        f"Text:\n{input_text}"
    )


def translate_text(client, input_text: str, target_language: str) -> str:
    prompt = build_translation_prompt(input_text, target_language)
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.5-flash").strip()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
    )
    translated_text = (getattr(response, "text", "") or "").strip()
    if not translated_text:
        raise ValueError("Gemini API returned an empty translation response.")
    return translated_text


def generate_speech(text: str, language_code: str) -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        temp_path = tmp.name
    try:
        tts = gTTS(text=text, lang=language_code)
        tts.save(temp_path)
        with open(temp_path, "rb") as file:
            return file.read()
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "source_text" not in st.session_state:
    st.session_state.source_text = ""
if "last_language" not in st.session_state:
    st.session_state.last_language = "Hindi"

client, client_error = get_gemini_client()

st.markdown(
    """
    <div class="hero-card">
        <h1 style="margin-bottom:0.3rem;">AI Translator and Speech Studio</h1>
        <p style="margin:0; font-size:1.05rem;">
            Translate text and documents into your selected language and generate downloadable speech output.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.markdown('<div class="info-card"><h4>Supported Inputs</h4><p>Manual text, PDF, TXT, CSV, XLSX, XLS</p></div>', unsafe_allow_html=True)
with metric2:
    st.markdown('<div class="info-card"><h4>Core AI Service</h4><p>Google Gemini API for translation</p></div>', unsafe_allow_html=True)
with metric3:
    st.markdown('<div class="info-card"><h4>Audio Output</h4><p>gTTS MP3 playback and download</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("User Guide")
    
    st.markdown(
        """
        **Steps**
        1. Ensure your Gemini API key is configured before using the app.
        2. Enter text or upload a supported file.
        3. Choose a target language.
        4. Click **Translate and Generate Speech**.
        5. Review translated text, play audio, and download outputs.
        """
    )
    st.caption("Supported file formats: PDF, TXT, CSV, XLSX, XLS")
    if client_error:
        st.warning(client_error)
    else:
        st.success("Gemini client initialized successfully.")

left, right = st.columns([1.1, 1])

with left:
    st.subheader("Input Workspace")
    input_mode = st.radio("Choose input method", ["Type text", "Upload file"], horizontal=True)
    raw_text = ""

    if input_mode == "Type text":
        raw_text = st.text_area(
            "Enter or paste text",
            height=280,
            placeholder="Example: Welcome to our capstone project. This app translates text and converts it into speech.",
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload a supported file",
            type=["pdf", "txt", "csv", "xlsx", "xls"],
        )
        if uploaded_file is not None:
            try:
                raw_text = extract_text_from_uploaded_file(uploaded_file)
                st.session_state.source_text = raw_text
                st.markdown('<div class="success-banner">File processed successfully. Extracted text preview is shown below.</div>', unsafe_allow_html=True)
                with st.expander("Preview extracted text"):
                    st.write(raw_text[:5000] if raw_text else "No text extracted.")
            except Exception as exc:
                st.error(f"File processing error: {exc}")

    selected_language = st.selectbox("Target language", list(LANGUAGE_OPTIONS.keys()), index=0)
    st.session_state.last_language = selected_language
    generate_now = st.button("Translate and Generate Speech", type="primary", use_container_width=True)

with right:
    st.subheader("Output Workspace")
    if generate_now:
        if client is None:
            st.error("Gemini client is not configured. Please add your API key first.")
        elif not raw_text or not raw_text.strip():
            st.error("Please type text or upload a readable file before translating.")
        else:
            try:
                source_text = raw_text.strip()
                st.session_state.source_text = source_text
                with st.spinner("Translating with Gemini API..."):
                    translated = translate_text(client, source_text, selected_language)
                language_code = get_language_code(selected_language)
                if not language_code:
                    raise ValueError(f"No gTTS language mapping found for {selected_language}.")
                with st.spinner("Creating speech audio with gTTS..."):
                    audio_bytes = generate_speech(translated, language_code)
                st.session_state.translated_text = translated
                st.session_state.audio_bytes = audio_bytes
                st.success("Translation and audio generation completed successfully.")
            except Exception as exc:
                st.error(f"Application error: {exc}")

    if st.session_state.source_text:
        st.text_area("Original text", st.session_state.source_text, height=140)
    if st.session_state.translated_text:
        st.text_area("Translated text", st.session_state.translated_text, height=180)
        st.download_button(
            "Download translated text",
            data=st.session_state.translated_text.encode("utf-8"),
            file_name=f"translated_{st.session_state.last_language.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True,
        )
    if st.session_state.audio_bytes:
        st.audio(st.session_state.audio_bytes, format="audio/mp3")
        st.download_button(
            "Download MP3 audio",
            data=st.session_state.audio_bytes,
            file_name=f"translated_{st.session_state.last_language.lower().replace(' ', '_')}.mp3",
            mime="audio/mpeg",
            use_container_width=True,
        )

