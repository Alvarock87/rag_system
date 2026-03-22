from app.ingetions.pipeline import IngestionPipeline
from app.ingetions.loaders.pdf_loader import PDFLoader

if __name__ == "__main__":

    pipeline = IngestionPipeline(PDFLoader())
    docs = pipeline.run("data/sample.pdf")

    print(docs[0].text[:500])