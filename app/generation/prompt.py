def build_prompt(query: str, context: str) -> str:
    return f"""
You are an expert assistant.

Answer the question using ONLY the context below.

Rules:
- Be precise and factual
- If the answer is incomplete, summarize clearly
- Do NOT copy text verbatim unless necessary
- If you don't know, say "I don't know"

Context:
{context}

Question:
{query}

Answer in a clear and complete sentence:
"""