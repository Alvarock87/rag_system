import re


class TextCleaner:
    def clean(self, text: str) -> str:
        text = text.strip()

        # eliminar múltiples espacios
        text = re.sub(r"\s+", " ", text)

        # eliminar caracteres raros
        text = re.sub(r"[^\x00-\x7F]+", " ", text)

        return text