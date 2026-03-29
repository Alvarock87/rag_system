from typing import List
from nltk.tokenize import sent_tokenize
from app.processing.schemas import Document, Chunk

class SemanticChunker:

    def __init__(self, chunk_size: int=800, overlap_sentences: int=2):
        self.chunk_size = chunk_size
        self.overlap_sentences = overlap_sentences


    def chunk(self, doc: Document) -> List[Chunk]:

        sentences = sent_tokenize(doc.text)

        chunks = []
        current_chunk = ""
        current_lenght = 0
        chunk_index = 0


        sentence_buffer = []

        for sentence in sentences:
            sentence_length = len(sentence)

            if current_lenght + sentence_length > self.chunk_size:
                chunks.append(
                    Chunk(
                        text=current_chunk.strip(),
                        metadata={
                            **doc.metadata,
                            "chunk_index": chunk_index,
                        }                        
                    )
                )
                chunk_index+=1

                sentence_buffer = sentence_buffer[-self.overlap_sentences :]
                current_chunk = " ".join(sentence_buffer)
                current_lenght = len(current_chunk)


            sentence_buffer.append(sentence)
            current_chunk += " " + sentence
            current_lenght += sentence_length

        if current_chunk.strip():
            chunks.append(
                Chunk(
                    text=current_chunk.strip(),
                    metadata={

                        **doc.metadata, 
                        "chunk_index": chunk_index,
                    }
                )
            )

        return chunks
