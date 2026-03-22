from app.ingetions.pipeline import IngestionPipeline
from app.ingetions.loaders.youtube_loader import YouTubeLoader



if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=aircAruvnKk"

    pipeline = IngestionPipeline(YouTubeLoader())
    docs = pipeline.run(url)

    print("TRANSCRIPTION PREVIEW:\n")
    print(docs[0].text[:500])

    print("\nMETADATA:\n")
    print(docs[0].metadata)