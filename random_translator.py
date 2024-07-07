import useful_functions
import song_scraper

import requests
from bs4 import BeautifulSoup, NavigableString
import re


song_titles_and_artists = song_scraper.scrape_billboard_hot_song_titles()

for i in range(len(song_titles_and_artists)):
    print(i, song_titles_and_artists[i][0], song_titles_and_artists[i][1])
    lyric_text = song_scraper.find_lyric_using_song_title_and_artist(
        song_titles_and_artists[i][0], song_titles_and_artists[i][1])
    print(lyric_text)
    print("----------------------------------------------------")

file_path = 'text.txt'

#useful_functions.translate_by_line(file_path, 'none', 5)
#useful_functions.translate_entire_file(file_path, 'simple', 5)




