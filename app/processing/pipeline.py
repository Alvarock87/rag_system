from typing import List
from app.processing.schemas import Document, Chunk
from app.processing.cleaner import TextCleaner
from app.processing.chunker import TextChunker
from app.processing.enricher import MetadataEnricher


class ProcessingPipeline:

    def __init__(self):
        self.cleaner = TextCleaner()
        self.chunker = TextChunker()
        self.enricher = MetadataEnricher()


    def run(self, docs: List[Document]) -> List[Chunk]:

        all_chunks = []

        for doc in docs:

            cleaned = self.cleaner.clean(doc.text)

            doc.text = cleaned

            chunks = self.chunker.chunk(doc)

            enriched_chunks = [self.enricher.enrich(c) for c in chunks]

            all_chunks.extend(enriched_chunks)

        return all_chunks