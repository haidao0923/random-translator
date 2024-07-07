import useful_functions
import song_scraper

import requests
from bs4 import BeautifulSoup, NavigableString
import re


#song_titles = song_scraper.scrape_billboard_hot_song_titles()

#for i in range(len(song_titles)):
#    print(i, song_titles[i])

lyric_text = song_scraper.find_lyric_using_song_title("Let it go")
print(lyric_text)

file_path = 'text.txt'

#useful_functions.translate_by_line(file_path, 'none', 5)
#useful_functions.translate_entire_file(file_path, 'simple', 5)




