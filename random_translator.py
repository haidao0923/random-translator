import useful_functions
import song_scraper
import requests
from bs4 import BeautifulSoup, NavigableString
import re

import os
from dotenv import load_dotenv


load_dotenv()

GENIUS_API_ACCESS_TOKEN = os.getenv("GENIUS_API_ACCESS_TOKEN")

#song_titles = song_scraper.scrape_billboard_hot_song_titles()

#for i in range(len(song_titles)):
#    print(i, song_titles[i])

search_response = requests.get('https://api.genius.com/search?q=A%20Bar%20Song%20(Tipsy)', headers={'Authorization': f'Bearer {GENIUS_API_ACCESS_TOKEN}'})
song_api_path = "https://api.genius.com" + search_response.json()["response"]["hits"][0]["result"]["api_path"]
print("Song API: ", song_api_path)
song_response = requests.get(song_api_path, headers={'Authorization': f'Bearer {GENIUS_API_ACCESS_TOKEN}'})
lyric_page_path = song_response.json()["response"]["song"]["url"]
print("Lyric Page", lyric_page_path)

lyric_response = requests.get(lyric_page_path)
soup = BeautifulSoup(lyric_response.content, 'html.parser')
lyric_container = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1")
text = lyric_container.get_text(strip=True, separator="\n")
print(text)

file_path = 'text.txt'

#useful_functions.translate_by_line(file_path, 'none', 5)
#useful_functions.translate_entire_file(file_path, 'simple', 5)




