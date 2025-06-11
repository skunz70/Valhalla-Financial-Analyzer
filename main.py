from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.brokerage_parser import parse_brokerage_pdf

app = FastAPI()

# Allow cross-origin requests (important for GPT connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/parse_brokerage")
async def parse_brokerage(file: UploadFile = File(...)):
    contents = await file.read()
    results = parse_brokerage_pdf(contents)
    return results

