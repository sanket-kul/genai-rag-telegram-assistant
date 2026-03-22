# 🚀 GenAI Mini-RAG Telegram Bot

> A production-ready Retrieval-Augmented Generation (RAG) system integrated with a Telegram bot, designed with modular architecture, efficient retrieval, and enterprise-grade best practices.

---

## 📌 Overview

This project demonstrates how to build a **scalable GenAI application** that combines:

* Semantic search using embeddings
* Context-aware generation using LLMs
* Conversational memory and caching
* Clean, extensible microservice-style architecture

The system enables users to interact via Telegram and receive **accurate, context-grounded responses** from a custom knowledge base.

---

## 🎯 Key Features

* 🤖 **Telegram Bot Interface**

  * `/ask <query>` → Query knowledge base
  * `/help` → Usage instructions
  * `/summarize` → Summarize recent interactions

* 🧠 **Mini-RAG Pipeline**

  * Document chunking
  * Embedding generation
  * Top-K semantic retrieval
  * Context-aware prompt construction

* 💬 **Conversation Memory**

  * Maintains last 3 interactions per user

* ⚡ **Caching Layer**

  * Avoids redundant embedding + LLM calls

* 📚 **Source Attribution**

  * Displays document snippets used in responses

* 🔌 **LLM Abstraction Layer**

  * Supports **Ollama (local)** and **OpenAI (cloud)**

* 🐳 **Containerized Deployment**

  * Docker-ready for consistent environments

---

## 🏗️ Architecture

```
User (Telegram)
      │
      ▼
Telegram Bot (Handlers)
      │
      ▼
RAG Pipeline
 ├── Retriever (Cosine Similarity)
 ├── Embedder (Sentence Transformers)
 ├── Vector Store (SQLite)
 ├── LLM Service (Ollama/OpenAI)
 │
 ├── Memory (Last N interactions)
 └── Cache (Query → Response)
      │
      ▼
Formatted Response (with sources)
```

---

## 🔄 RAG Workflow

1. **Document Ingestion**

   * Load Markdown/Text files
   * Split into chunks

2. **Embedding Generation**

   * Use lightweight transformer model (MiniLM)

3. **Storage**

   * Persist embeddings in SQLite

4. **Query Handling**

   * Embed user query
   * Retrieve top-K relevant chunks
   * Construct prompt with:

     * Context
     * Chat history
     * User query

5. **LLM Inference**

   * Generate grounded response

6. **Response Formatting**

   * Return answer + source snippets

---

## 🛠️ Tech Stack

| Layer          | Technology                |
| -------------- | ------------------------- |
| Bot Interface  | python-telegram-bot       |
| Embeddings     | sentence-transformers     |
| Vector Storage | SQLite                    |
| LLM            | Ollama (Mistral) / OpenAI |
| Backend        | Python                    |
| Similarity     | NumPy (Cosine Similarity) |
| Deployment     | Docker                    |

---

## 📁 Project Structure

```
genai-rag-bot/
│
├── app/
│   ├── main.py                # Entry point
│   ├── config.py             # Configuration
│   │
│   ├── bot/                  # Telegram bot layer
│   │   ├── telegram_bot.py
│   │   └── handlers.py
│   │
│   ├── rag/                  # RAG pipeline
│   │   ├── pipeline.py
│   │   ├── retriever.py
│   │   ├── embedder.py
│   │   └── vector_store.py
│   │
│   ├── llm/                  # LLM abstraction
│   │   └── llm_service.py
│   │
│   ├── memory/               # Conversation memory
│   │   └── chat_memory.py
│   │
│   ├── cache/                # Caching layer
│   │   └── cache.py
│   │
│   ├── utils/                # Utility functions
│   │   └── chunking.py
│   │
│   └── data/                 # Data storage
│       ├── docs/
│       └── db.sqlite
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd genai-rag-bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Start Local LLM (Ollama)

```bash
ollama run mistral
```

---

### 4. Configure Environment Variables

```bash
export TELEGRAM_TOKEN=your_telegram_token
export OPENAI_API_KEY=your_openai_key  # optional
```

---

### 5. Run Application

```bash
python -m app.main
```

---

## 🤖 Bot Usage

| Command        | Description                 |
| -------------- | --------------------------- |
| `/ask <query>` | Ask a question using RAG    |
| `/help`        | Display usage instructions  |
| `/summarize`   | Summarize last conversation |

---

## ⚡ Performance & Optimization

* Efficient **embedding model (MiniLM)** for low latency
* **Cosine similarity** for fast retrieval
* **In-memory caching** for repeated queries
* Limited **context window** to optimize LLM calls
* Lightweight **SQLite storage** for portability

---

## 🧪 Evaluation Alignment

| Criteria      | Implementation                          |
| ------------- | --------------------------------------- |
| Code Quality  | Modular, readable, extensible           |
| System Design | Clear separation of concerns            |
| Model Usage   | Efficient local + API-based LLM support |
| Efficiency    | Caching + lightweight models            |
| UX            | Fast, contextual, transparent responses |

---

## 📸 Demo (Recommended)

Include:

* Telegram interaction screenshot
* Query-response flow
* Source attribution example

Example:

```
User: /ask What is refund policy?
Bot: Refunds are processed within 7 days...

Sources:
- policy.md
```

---

## 🚀 Future Enhancements

* FAISS / Chroma vector database
* Redis-based distributed caching
* FastAPI backend for scalability
* Streaming responses (token-wise)
* Multi-agent workflows (LangGraph)
* RAG evaluation (RAGAS framework)

---

## 🧠 Design Rationale

| Decision             | Reason                      |
| -------------------- | --------------------------- |
| SQLite               | Zero external dependency    |
| MiniLM               | Fast + efficient embeddings |
| Ollama               | Local inference, no cost    |
| Modular architecture | Easy scaling & testing      |
| LLM abstraction      | Vendor flexibility          |

---

## 🔐 Production Considerations

* Add structured logging (e.g., `loguru`)
* Implement retry + timeout handling
* Add rate limiting for bot endpoints
* Secure API keys via environment variables
* Integrate monitoring (Prometheus/Grafana)

---

## 👨‍💻 Author

**Sanket Kulkarni**
AI Engineer | GenAI Developer

* GitHub: https://github.com/sanket-kul
* LinkedIn: https://www.linkedin.com/in/sanketkul/

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ and contributing!

---

## 📄 License

This project is for educational and assessment purposes.
