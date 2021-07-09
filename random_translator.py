import random
from deep_translator import GoogleTranslator

original_text = "Let it go"
translated = original_text

random.shuffle(GoogleTranslator.get_supported_languages())

for x in GoogleTranslator.get_supported_languages():
    translated = GoogleTranslator(source='auto', target=x).translate(translated)
    print(f'''{x} -> {GoogleTranslator(source='auto', target='en').translate(translated)}''')

translated = GoogleTranslator(source='auto', target='en').translate(translated)
print(f'original -> {original_text}')
print(f'en -> {translated}')
