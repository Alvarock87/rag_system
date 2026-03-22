import os
import subprocess
import whisper
from typing import List
from app.ingetions.loaders.base import BaseLoader
from app.ingetions.schemas import Document

class YouTubeLoader(BaseLoader):

    def load(self, url:str) -> List[Document]:

        output_template = "data/tmp/temp_audio.%(ext)s"

        # descargar audio
        subprocess.run(
            ["yt-dlp", 
             "-x", 
             "--audio-format", 
             "mp3", 
             "-o", 
             output_template, 
             url,
             ],
            check=True
        )

        # transcribir
        audio_file = None
        for file in os.listdir():
            if file.startswith("temp_audio") and file.endswith(".mp3"):
                audio_file = file
                break

        if not audio_file:
            raise RuntimeError("Audio file not found after download")


        # Transcribir
        model = whisper.load_model("base")
        result = model.transcribe(audio_file)

        os.remove(audio_file)

        return [
            Document(
                text = result["text"],
                metadata={
                    "source":url,
                    "type": "youtube",
                },
            )
            ]