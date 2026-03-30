from app.generation.rag import RAG

if __name__ == "__main__":

    rag = RAG()

    questions = "who is dracula?"

    answer = rag.ask(questions)

    print("\nAnswer:\n")
    print(answer)