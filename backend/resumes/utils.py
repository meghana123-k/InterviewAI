import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF using PyMuPDF.
    """

    text = ""

    document = fitz.open(pdf_path)

    try:
        for page in document:
            text += page.get_text()

    finally:
        document.close()

    return text.strip()
