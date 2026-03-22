from collections import defaultdict, deque

class ChatMemory:
    def __init__(self, max_history=3):
        self.memory = defaultdict(lambda: deque(maxlen=max_history))

    def add(self, user_id, query, response):
        self.memory[user_id].append((query, response))

    def get(self, user_id):
        return list(self.memory[user_id])