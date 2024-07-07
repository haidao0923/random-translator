import random
import itertools
from deep_translator import GoogleTranslator

def translate_entire_file(file_path, debug_style, n=10):
    file = open(file_path)
    text = file.read()
    file.close()

    translated_text = translate(text, debug_style, n)
    write_to_file(translated_text)

def translate_by_line(file_path, debug_style, n=10):
    file = open(file_path)
    lines = file.read().splitlines()
    file.close()

    translated_lines = []
    for line in lines:
        translated_lines.append(translate(line, debug_style, n))

    translated_text = ""
    for line in translated_lines:
        translated_text += line + "\n"

    write_to_file(translated_text)

def translate(text, debug_style, n):
    if text == '':
        return '\n'
    original_text = text
    # randomized the languages to be translated
    random.shuffle(GoogleTranslator.get_supported_languages())
    # translate with the first n random languages
    for language in itertools.islice(GoogleTranslator.get_supported_languages(), n):
        text = GoogleTranslator(source='auto', target=language).translate(text)
        debug_type(debug_style, language, text)
    return translate_back_into_english(original_text, text)

def debug_type(option, x, text):
    function_dict = {'english' : debug_english,
                     'simple'  : debug_simple,
                     'none'    : lambda x,y:None
    }
    function_dict[option](x, text)

def debug_english(x, text):
    print(f'''{x} -> {GoogleTranslator(source='auto', target='en').translate(text)}''')
    print('=====================')

def debug_simple(x, text):
    print(f'{x} -> {text}')
    print('=====================')

def translate_back_into_english(original_text, text):
    text = GoogleTranslator(source='auto', target='en').translate(text)
    print(f'original -> {original_text}')
    print('=====================')
    print(f'en -> {text}\n')
    return text

def write_to_file(text):
    file = open("translated_lyric.txt", "w")
    file.write(text)
    file.close()