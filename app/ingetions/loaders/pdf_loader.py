import fitz
from typing import List
from app.ingetions.loaders.base import BaseLoader
from app.ingetions.schemas import Document

class PDFLoader(BaseLoader):

    def load(self, file_path:str) -> List[Document]:

        docs = []
        pdf = fitz.open(file_path)

        for i, page in enumerate(pdf):

            text = page.get_text()

            docs.append(
                Document(
                    text = text,
                    metadata = {
                        "source":file_path, 
                        "page": i,
                        "type": "pdf",
                    }
                )
            )

        return docs