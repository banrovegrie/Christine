from googletrans import Translator

def translation(text):
    translator = Translator()

    if translator.detect(text).lang != 'en':
        text = translator.translate(text).text
    return text

