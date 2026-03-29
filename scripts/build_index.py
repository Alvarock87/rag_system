from app.ingetions.pipeline import IngestionPipeline
from app.ingetions.loaders.web_loader import WebLoader
from app.processing.pipeline import ProcessingPipeline
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


if __name__ == "__main__":

    ingestion = IngestionPipeline(WebLoader())
    docs = ingestion.run("https://www.gutenberg.org/files/345/345-h/345-h.htm")

    procesor = ProcessingPipeline()
    chunks = procesor.run(docs)

    print(f"Chunks: {len(chunks)}")


    embedder = Embedder()
    texts = [c.text for c in chunks]
    embeddings = embedder.encode(texts)

    store = ChromaStore()
    store.add(chunks, embeddings)

    print("Index build done!")