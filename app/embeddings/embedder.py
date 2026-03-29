from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class Embedder:

    def __init__(self, model_name:str = "BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)


    def encode(self, texts: List[str]) -> List[List[float]]:

        embeddings = self.model.encode(texts)

        embeddings = np.array(embeddings)
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

        return embeddings.tolist()