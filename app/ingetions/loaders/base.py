from abc import ABC, abstractmethod
from typing import List
from app.ingetions.schemas import Document

class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> List[Document]:
        """Load documents and return a list of Document objects."""
        pass

    