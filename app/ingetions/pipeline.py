from typing import List
from app.ingetions.schemas import Document

class IngestionPipeline:

    def __init__(self, loader):
        self.loader = loader

    
    def run(self, source:str) -> List[Document]:

        docs = self.loader.load(source)


        return docs