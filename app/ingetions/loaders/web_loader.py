import requests
from bs4 import BeautifulSoup
from app.ingetions.schemas import Document
from app.ingetions.loaders.base import BaseLoader


class WebLoader(BaseLoader):

    def load(self, url:str) -> list[Document]:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style", "header", "footer", "nav"]):
            script.extract()

        text = soup.get_text(separator=" ")

        return [Document(
            text = text, 
            metadata={
                "source": url, 
                "type": "web",
            }
        )]

