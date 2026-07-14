LANGUAGE_OPTIONS = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Tamil": "ta",
    "Telugu": "te",
}


def get_language_code(language_name: str) -> str:
    return LANGUAGE_OPTIONS.get(language_name, "")
