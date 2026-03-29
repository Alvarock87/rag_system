import chromadb
from typing import List
from app.processing.schemas import Chunk

class ChromaStore:


    def __init__(self, persist_dir: str= "data/chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_dir) 

        self.collection = self.client.get_or_create_collection(
            name="rag_collection"
        )


    def add(self, chunks: List[Chunk], embeddings: List[List[float]]):

        texts = [c.text for c in chunks]
        metadatas = [c.metadata for c in chunks]
        ids = [f"chunk_{i}" for i in range(len(chunks))]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )


    def search(self, query_embedding: List[float], k: int = 5):

        print("Collection count:", self.collection.count())

        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        return result