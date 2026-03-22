from google import genai
from app.config import settings

class Embedder:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)
        self.model = settings.EMBEDDING_MODEL

        # Embedding cache
        self.cache = {}

    def embed(self, texts):
        """
        Input: List[str]
        Output: List[List[float]]
        """

        results = [None] * len(texts)
        texts_to_fetch = []
        index_map = {}

        # Check cache
        for idx, text in enumerate(texts):
            if text in self.cache:
                results[idx] = self.cache[text]
            else:
                index_map[len(texts_to_fetch)] = idx
                texts_to_fetch.append(text)

        # Fetch uncached
        if texts_to_fetch:
            response = self.client.models.embed_content(
                model=self.model,
                contents=texts_to_fetch
            )

            for i, emb in enumerate(response.embeddings):
                original_idx = index_map[i]
                embedding = emb.values

                self.cache[texts_to_fetch[i]] = embedding
                results[original_idx] = embedding

        return results