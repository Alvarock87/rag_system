from app.retrieval.retriever import Retriever
from app.generation.llm_local import LLM
from app.generation.prompt import build_prompt


class RAG:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM(model="llama3:instruct")


    def ask(self, query:str):

        results = self.retriever.retrieval(query)

        docs = [doc for doc, _ in results]

        context = "\n\n".join(docs[:3])

        promtp = build_prompt(query, context)

        answer = self.llm.generate(promtp)

        return answer