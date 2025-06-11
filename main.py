from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.brokerage_parser import parse_brokerage_pdf
from utils.statement_parser import parse_financial_pdf

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
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.statement_parser import parse_financial_pdf

app = FastAPI()

@app.post("/parse_statement")
async def parse_statement(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = parse_financial_statement(contents)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
from fastapi import UploadFile, File

@app.post("/parse_statement")
async def parse_statement(file: UploadFile = File(...)):
    contents = await file.read()
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)

    parsed = parse_financial_pdf(temp_path)
    return parsed
@app.post("/parse_statement")
async def parse_statement(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)

        # Call your generalized PDF parsing function
        parsed = parse_financial_pdf(temp_path)

        return {"parsed_data": parsed}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

