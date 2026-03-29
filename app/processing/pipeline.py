from typing import List
from app.processing.schemas import Document, Chunk
from app.processing.cleaner import TextCleaner
from app.processing.semantic_chunker import SemanticChunker
from app.processing.enricher import MetadataEnricher


class ProcessingPipeline:

    def __init__(self):
        self.cleaner = TextCleaner()
        self.chunker = SemanticChunker()
        self.enricher = MetadataEnricher()


    def run(self, docs: List[Document]) -> List[Chunk]:

        all_chunks = []

        for doc in docs:

            cleaned = self.cleaner.clean(doc.text)

            doc.text = cleaned

            chunks = self.chunker.chunk(doc)

            chunks = [c for c in chunks if len(c.text.strip()) > 200]

            enriched_chunks = [self.enricher.enrich(c) for c in chunks]

            all_chunks.extend(enriched_chunks)

            print(f"Total chunks: {len(chunks)}")
            print(f"Avg length: {sum(len(c.text) for c in chunks) / len(chunks):.2f}")

        return all_chunks