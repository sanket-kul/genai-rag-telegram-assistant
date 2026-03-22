from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

docs_url="/docs",
redoc_url="/redoc",
openapi_tags=[
    {"name": "RAG", "description": "Retrieval-Augmented Generation APIs"},
    {"name": "Utility", "description": "Helper endpoints"}
]

app = FastAPI(
    title="GenAI RAG Assistant API",
    description="""
### 🚀 Production-grade Retrieval-Augmented Generation (RAG) API

This API enables:
- Semantic search over custom knowledge base
- Context-aware responses using LLM (Groq)
- Conversation memory (last N interactions)
- Query caching for performance optimization

---

### 🔑 Core Features
- 📚 RAG (Retrieval-Augmented Generation)
- ⚡ Fast inference via Groq LLM
- 🧠 Conversational memory
- 📊 Source-grounded responses
- 🔁 Intelligent caching

---

### 📌 Available Endpoints
- `/ask` → Ask questions using RAG
- `/summarize` → Summarize recent conversation
- `/help` → API usage guide
    """,
    version="1.0.0"
)

pipeline = None


# =========================
# Request Schema
# =========================
class QueryRequest(BaseModel):
    user_id: str = Field(
        ...,
        description="Unique identifier for the user",
        examples=["user_123"]
    )
    query: str = Field(
        ...,
        description="User question",
        examples=["What is leave policy?"]
    )


# =========================
# ASK ENDPOINT
# =========================
@app.post(
    "/ask",
    summary="Ask a question (RAG-enabled)",
    description="""
Submit a query to the system.

### 🔍 What happens internally:
1. Query is embedded using Google embeddings  
2. Relevant chunks are retrieved from vector DB  
3. Context + history is sent to LLM (Groq)  
4. Response is generated with sources  

### 📥 Input:
- user_id → Unique user identifier
- query → Natural language question

### 📤 Output:
- AI-generated answer with source references
    """
)
def ask(req: QueryRequest):
    return {
        "response": pipeline.run(req.user_id, req.query)
    }


# =========================
# SUMMARIZE ENDPOINT
# =========================
@app.post(
    "/summarize",
    summary="Summarize conversation",
    description="""
Generates a summary of the last few interactions for a user.

### 🧠 Uses:
- Chat memory (last N messages)
- LLM summarization

### 📥 Input:
- user_id → Unique user identifier

### 📤 Output:
- Concise summary including key insights
    """
)
def summarize(
    user_id: str = Query(
    ...,
    description="Unique user identifier",
    examples={"default": {"value": "user_123"}}
)):
    
    return {
        "summary": pipeline.summarize(user_id)
    }


# =========================
# HELP ENDPOINT
# =========================
@app.get(
    "/help",
    summary="API usage guide",
    description="""
Provides a quick guide on how to use the API endpoints.

Useful for:
- First-time users
- Debugging
- Understanding available capabilities
    """
)
def help():
    return {
        "message": "Welcome to GenAI RAG Assistant API",
        "endpoints": {
            "/ask": {
                "method": "POST",
                "description": "Ask a question using RAG",
                "payload": {
                    "user_id": "string",
                    "query": "string"
                }
            },
            "/summarize": {
                "method": "POST",
                "description": "Summarize last conversation",
                "params": {
                    "user_id": "string"
                }
            },
            "/help": {
                "method": "GET",
                "description": "Show API usage"
            }
        }
    }


# =========================
# PIPELINE INJECTION
# =========================
def set_pipeline(p):
    global pipeline
    pipeline = p