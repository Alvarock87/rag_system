import requests
from bs4 import BeautifulSoup
from app.ingetions.schemas import Document
from app.ingetions.loaders.base import BaseLoader
import re

class WebLoader(BaseLoader):

    def load(self, url:str) -> list[Document]:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.extract()

        main_content = soup.find("body")

        if main_content:
            text = main_content.get_text(separator=" ")
        else:
            text = soup.get_text(separator=" ")

        # eliminar líneas muy cortas
        lines = [line.strip() for line in text.split("\n")]
        lines = [line for line in lines if len(line) > 50]

        text = " ".join(lines)
        text = re.sub(r"\s+", " ", text)

        # eliminar patrones basura
        text = re.sub(r"CHAPTER\s+[IVXLCDM]+", " ", text)
        text = re.sub(r"Copyright.*?Project Gutenberg", " ", text)

        return [Document(
            text = text, 
            metadata={
                "source": url, 
                "type": "web",
            }
        )]

