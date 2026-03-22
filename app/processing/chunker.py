from typing import List
from app.processing.schemas import Document, Chunk


class TextChunker:

    def __init__(self, chunk_size: int = 500, overlap: int = 100):

        self.chunk_size = chunk_size
        self.overlap = overlap


    def split_text(self, text:str) -> List[str]:

        chunks = []
        start = 0

        while start < len(text):

            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks
    

    def chunk(self, doc:Document) -> List[Chunk]:

        texts = self.split_text(doc.text)


        return [
            Chunk(
                text=t,
                metadata={
                    **doc.metadata,
                    "chunk_index": i, 
                },
            )
            for i, t in enumerate(texts)
        ]