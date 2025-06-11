import pdfplumber
import io

def parse_brokerage_pdf(contents: bytes) -> dict:
    text = ""
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    text = text.lower()
    summary = {
        "capital_gains": "not found",
        "dividends": "not found",
        "qualified_dividends": "not found",
        "asset_breakdown": []
    }

    if "capital gains" in text:
        summary["capital_gains"] = "Capital gains detected"
    if "ordinary dividends" in text or "total dividends" in text:
        summary["dividends"] = "Ordinary dividends detected"
    if "qualified dividends" in text:
        summary["qualified_dividends"] = "Qualified dividends detected"
    if "asset allocation" in text:
        summary["asset_breakdown"].append("Asset allocation section found")

    return summary
added brokerage_parser utility
