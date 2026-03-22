from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="GenAI RAG API")

pipeline = None


class QueryRequest(BaseModel):
    user_id: str
    query: str


@app.post("/ask")
def ask(req: QueryRequest):
    return {"response": pipeline.run(req.user_id, req.query)}


@app.post("/summarize")
def summarize(user_id: str):
    return {"summary": pipeline.summarize(user_id)}


def set_pipeline(p):
    global pipeline
    pipeline = p