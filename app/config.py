import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    # Google Embeddings
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    # Groq LLM
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL")

    # RAG Config
    TOP_K = int(os.getenv("TOP_K", 3))
    MAX_HISTORY = int(os.getenv("MAX_HISTORY", 3))
    DB_PATH = os.getenv("DB_PATH", "app/data/db.sqlite")

settings = Settings()