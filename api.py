from tempfile import SpooledTemporaryFile
from typing import Optional

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

from src.pipeline import run_pipeline


app = FastAPI(
    title="Self-RAG Evidence Assistant API",
    description="A simple FastAPI backend for the Self-RAG Evidence Assistant project.",
    version="1.0.0",
)


class AskRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3
    min_score: Optional[float] = 0.25


class APIUploadFile:
    def __init__(self, name: str, file: SpooledTemporaryFile):
        self.name = name
        self.file = file

    def read(self, *args, **kwargs):
        return self.file.read(*args, **kwargs)

    def seek(self, *args, **kwargs):
        return self.file.seek(*args, **kwargs)

    def tell(self):
        return self.file.tell()


@app.get("/")
def root():
    return {
        "message": "Self-RAG Evidence Assistant API is running.",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Self-RAG Evidence Assistant API",
    }


@app.post("/ask")
def ask_question(request: AskRequest):
    result = run_pipeline(
        uploaded_files=[],
        question=request.question,
        top_k=request.top_k,
        min_score=request.min_score,
    )

    return result


@app.post("/ask-file")
async def ask_question_with_file(
    question: str = Form(...),
    top_k: int = Form(3),
    min_score: float = Form(0.25),
    file: UploadFile = File(...),
):
    temp_file = SpooledTemporaryFile()
    temp_file.write(await file.read())
    temp_file.seek(0)

    uploaded_files = [
        APIUploadFile(
            name=file.filename,
            file=temp_file,
        )
    ]   

    result = run_pipeline(
        uploaded_files=uploaded_files,
        question=question,
        top_k=top_k,
        min_score=min_score,
    )

    return result