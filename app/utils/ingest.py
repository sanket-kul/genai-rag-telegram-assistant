import os
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.config import settings

DOCS_PATH = "app/data/docs"


def load_documents():
    docs = []

    if not os.path.exists(DOCS_PATH):
        return docs

    for file in os.listdir(DOCS_PATH):
        file_path = os.path.join(DOCS_PATH, file)

        if file.endswith(".md") or file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                docs.append((file, f.read()))

    return docs


def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def ingest_if_needed():
    store = VectorStore(settings.DB_PATH)

    # ✅ Check if DB already has data
    existing = store.fetch_all()
    if existing:
        print("⚡ Embeddings already exist. Skipping ingestion.")
        return

    print("🚀 Running document ingestion...")

    embedder = Embedder()
    documents = load_documents()

    for filename, doc in documents:
        chunks = chunk_text(doc)
        embeddings = embedder.embed(chunks)

        for chunk, emb in zip(chunks, embeddings):
            store.insert(f"[{filename}] {chunk}", emb)

    print("✅ Ingestion completed.")