import os
try:
    from googletrans import Translator
except:
    os.system('pip3 install googletrans')
    from googletrans import Translator

def translation(text):
    translator = Translator()

    if translator.detect(text).lang != 'en':
        text = translator.translate(text).text
    return text

