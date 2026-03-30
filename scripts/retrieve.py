from app.retrieval.retriever import Retriever


if __name__ == "__main__":

    retriever = Retriever()

    query = "Who is Dracula?"

    results = retriever.retrieval(query)

    print("\nFinal Results:\n")

    for doc, score in results:
        print(f"Score: {score:.4f}")
        print(doc[:300])
        print("\n---\n")