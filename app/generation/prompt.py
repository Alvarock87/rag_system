def build_prompt(query:str, context:str) -> str:

    return f"""
you're a helpful assitant.

Answer the questions based ONLY on the context below.
If the answer is not in the context, say "i don't have enought knowedge to answer this"

Context:
{context}

Question:
{query}

Answer:
"""