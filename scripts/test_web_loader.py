from app.ingetions.pipeline import IngestionPipeline
from app.ingetions.loaders.web_loader import WebLoader


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Medicine"

    pipeline = IngestionPipeline(WebLoader())
    docs = pipeline.run(url)

    print("TEXT PREVIEW:\n")
    print(docs[0].text[:500])

    print("\nMETADATA:\n")
    print(docs[0].metadata)