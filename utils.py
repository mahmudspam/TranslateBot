from googletrans import Translator , LANGCODES


tr = Translator()


async def translate_text(text: str, lang: str):
    return tr.translate(text=text,dest=lang).text