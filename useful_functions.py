import random
import itertools
from deep_translator import GoogleTranslator

def translate_entire_file(file_path, debug_style, n=10):
    file = open(file_path)
    text = file.read()
    file.close()

    translate(text, debug_style, n)

def translate_by_line(file_path, debug_style, n=10):
    file = open(file_path)
    lines = file.read().splitlines()
    file.close()

    final_list = []
    for line in lines:
        final_list += [translate(line, debug_style, n)]
    for line in final_list:
        print(line)

def translate(text, debug_style, n):
    if text == '':
        return '\n'
    original_text = text
    # randomized the languages to be translated
    random.shuffle(GoogleTranslator.get_supported_languages())
    # translate with the first n random languages
    for x in itertools.islice(GoogleTranslator.get_supported_languages(), n):
        text = GoogleTranslator(source='auto', target=x).translate(text)
        debug_type(debug_style, x, text)
    return translate_back_into_english(original_text, text)
    
def debug_type(option, x, text):
    function_dict = {'english' : debug_english,
                     'simple'  : debug_simple,
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
