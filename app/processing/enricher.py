from app.processing.schemas import Chunk

class MetadataEnricher:

    def enrich(self, chunk:Chunk) -> Chunk:

        chunk.metadata["length"] = len(chunk.text)
        chunk.metadata["preview"] = chunk.text[:50]

        return chunk