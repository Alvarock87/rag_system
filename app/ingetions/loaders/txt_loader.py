from typing import List
from app.ingetions.loaders.base import BaseLoader
from app.ingetions.schemas import Document

class TXTLoader(BaseLoader):

    def load(self, file_path:str) -> List[Document]:

        with open(file_path, "r") as f:
            text = f.read()

        return [
            Document(
                text=text,
                metadata={
                    "source":file_path, 
                    "type": "txt",
                },
            )
        ]