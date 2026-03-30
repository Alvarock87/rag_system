from app.retrieval.hybrid_search import HybridSearch
from app.retrieval.reranker import Reranker


class Retriever:

    def __init__(self):
        self.search = HybridSearch()
        self.reranker = Reranker()


    def retrieval(self, query:str, k: int = 5):

        results = self.search.search(query=query, k=20)

        docs = results["documents"][0]

        ranked = self.reranker.rerank(query, docs)

        return ranked[:k]