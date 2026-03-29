from typing import List
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


class HybridSearch:

    def __init__(self):
        self.embedder = Embedder()
        self.store = ChromaStore()


    def search(self, query: str, k:int=10):

        query_embedding = self.embedder.encode([query])[0]

        results = self.store.search(query_embedding, 5)

        return results
