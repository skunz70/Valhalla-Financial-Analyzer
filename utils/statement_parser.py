from PyPDF2 import PdfReader

def parse_financial_pdf(file_path: str) -> dict:
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Dummy logic – to be replaced with intelligent parsing later
        lines = text.splitlines()
        summary = "\n".join(lines[:20])  # Sample first 20 lines

        return {
            "statement_type": "generic",
            "summary": summary,
        }
    except Exception as e:
        return {"error": str(e)}
