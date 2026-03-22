import sqlite3
import json

class VectorStore:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY,
            text TEXT,
            embedding TEXT
        )
        """)

    def insert(self, text, embedding):
        self.conn.execute(
            "INSERT INTO embeddings (text, embedding) VALUES (?, ?)",
            (text, json.dumps(embedding))
        )
        self.conn.commit()

    def fetch_all(self):
        return self.conn.execute("SELECT text, embedding FROM embeddings").fetchall()

    def count(self):
        return self.conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]