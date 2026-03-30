from sentence_transformers import CrossEncoder
from typing import List

class Reranker:

    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


    def rerank(self, query: str, documents: List[str]):

        pairs = [(query, doc) for doc in documents]

        scores = self.model.predict(pairs)

        ranker = sorted(
            zip(documents, scores),
            key=lambda x: x[1], reverse=True, 
        )

        return ranker
