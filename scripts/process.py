from app.processing.pipeline import ProcessingPipeline
from app.ingetions.loaders.web_loader import WebLoader
from app.ingetions.pipeline import IngestionPipeline


if __name__ == "__main__":

    ingestion = IngestionPipeline(WebLoader())
    docs = ingestion.run("https://www.gutenberg.org/files/345/345-h/345-h.htm")

    processor = ProcessingPipeline()
    chunks = processor.run(docs)

    print(f"Total chunks: {len(chunks)}\n")

    print("Sample chunk:\n")
    print(chunks[0].text[:300])

    print("\nMetadata:\n")
    print(chunks[0].metadata)
