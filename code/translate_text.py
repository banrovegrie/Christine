import os

try:
    from googletrans import Translator
except:
    os.system('pip3 install googletranslate')

def translation(text):
    
