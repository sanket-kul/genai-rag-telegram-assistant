import threading
import uvicorn

from app.config import settings
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.llm.llm_service import LLMService
from app.memory.chat_memory import ChatMemory
from app.cache.cache import SimpleCache
from app.rag.pipeline import RAGPipeline
from app.bot.telegram_bot import run_bot
from app.api.main import set_pipeline
from app.ui.gradio_app import create_ui
from app.utils.ingest import ingest_if_needed


def create_pipeline():
    embedder = Embedder()
    store = VectorStore(settings.DB_PATH)
    retriever = Retriever(store, embedder)

    llm = LLMService()
    memory = ChatMemory(settings.MAX_HISTORY)
    cache = SimpleCache()

    return RAGPipeline(retriever, llm, memory, cache)


def run_fastapi():
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000)


def main():
    # ✅ Auto ingestion
    ingest_if_needed()

    # Create pipeline
    pipeline = create_pipeline()

    # Inject into FastAPI
    set_pipeline(pipeline)

    # Run FastAPI in background
    threading.Thread(target=run_fastapi, daemon=True).start()

    # Start Gradio UI
    ui = create_ui(pipeline)
    threading.Thread(
        target=lambda: ui.launch(server_name="0.0.0.0", server_port=7860),
        daemon=True).start()

    # Run Telegram bot (blocking)
    run_bot(pipeline)


if __name__ == "__main__":
    main()