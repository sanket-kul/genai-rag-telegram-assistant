import numpy as np
import json

class Retriever:
    def __init__(self, vector_store, embedder):
        self.store = vector_store
        self.embedder = embedder

    def retrieve(self, query, top_k=3):
        query_vec = np.array(self.embedder.embed([query])[0])

        data = self.store.fetch_all()
        scores = []

        for text, emb in data:
            emb_vec = np.array(json.loads(emb))
            sim = np.dot(query_vec, emb_vec) / (
                np.linalg.norm(query_vec) * np.linalg.norm(emb_vec)
            )
            scores.append((text, sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]