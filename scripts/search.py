from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


if __name__ == "__main__":

    query = "who is dracula?"

    embedder = Embedder()
    store = ChromaStore()

    query_embedding = embedder.encode([query])[0]

    results = store.search(query_embedding=query_embedding)

    print("\n Top results: \n")

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(meta)
        print(doc[:300])
        print("\n---\n")