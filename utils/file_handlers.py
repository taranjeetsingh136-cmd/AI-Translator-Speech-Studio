import io

import pandas as pd
from PyPDF2 import PdfReader

SUPPORTED_EXTENSIONS = {"pdf", "txt", "csv", "xlsx", "xls"}


def read_txt(file_bytes: bytes) -> str:
    text = file_bytes.decode("utf-8", errors="ignore").strip()
    if not text:
        raise ValueError("The TXT file is empty or unreadable.")
    return text


def read_csv(file_bytes: bytes) -> str:
    df = pd.read_csv(io.BytesIO(file_bytes))
    if df.empty:
        raise ValueError("The CSV file contains no readable rows.")
    return df.fillna("").astype(str).to_string(index=False)


def read_excel(file_bytes: bytes) -> str:
    excel = pd.ExcelFile(io.BytesIO(file_bytes))
    collected = []
    for sheet in excel.sheet_names:
        df = pd.read_excel(excel, sheet_name=sheet)
        if not df.empty:
            collected.append(f"Sheet: {sheet}\n{df.fillna('').astype(str).to_string(index=False)}")
    final_text = "\n\n".join(collected).strip()
    if not final_text:
        raise ValueError("The Excel file is empty or unreadable.")
    return final_text


def read_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        if text.strip():
            pages.append(text.strip())
    final_text = "\n\n".join(pages).strip()
    if not final_text:
        raise ValueError("The PDF file does not contain extractable text.")
    return final_text


def extract_text_from_uploaded_file(uploaded_file) -> str:
    extension = uploaded_file.name.lower().split(".")[-1]
    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file type. Upload PDF, TXT, CSV, XLSX, or XLS only.")
    file_bytes = uploaded_file.read()
    if not file_bytes:
        raise ValueError("The uploaded file is empty.")
    if extension == "txt":
        return read_txt(file_bytes)
    if extension == "csv":
        return read_csv(file_bytes)
    if extension in {"xlsx", "xls"}:
        return read_excel(file_bytes)
    if extension == "pdf":
        return read_pdf(file_bytes)
    raise ValueError("Unsupported file type encountered during processing.")
