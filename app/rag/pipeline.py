from app.config import settings

class RAGPipeline:
    def __init__(self, retriever, llm, memory, cache):
        self.retriever = retriever
        self.llm = llm
        self.memory = memory
        self.cache = cache

    def run(self, user_id, query):
        cached = self.cache.get(query)
        if cached:
            return cached

        docs = self.retriever.retrieve(query, settings.TOP_K)

        context = "\n".join([d[0] for d in docs])
        sources = [d[0][:80] for d in docs]

        history = self.memory.get(user_id)
        history_text = "\n".join([f"Q:{q} A:{a}" for q, a in history])

        prompt = f"""
        Use the following context to answer the question.

        Context:
        {context}

        Conversation History:
        {history_text}

        Question:
        {query}

        Provide a clear and concise answer.
        """

        answer = self.llm.generate(prompt)

        self.memory.add(user_id, query, answer)
        self.cache.set(query, answer)

        return answer + "\n\nSources:\n" + "\n".join(sources)

    def summarize(self, user_id):
        history = self.memory.get(user_id)

        if not history:
            return "No conversation history to summarize."

        history_text = "\n".join(
            [f"Q: {q}\nA: {a}" for q, a in history]
        )

        prompt = f"""
        You are an AI assistant.

        Summarize the following conversation into:
        - Key topics
        - Important insights
        - Actionable points (if any)

        Conversation:
        {history_text}

        Summary:
        """

        return self.llm.generate(prompt)