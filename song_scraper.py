import requests
from bs4 import BeautifulSoup, NavigableString
import os
from dotenv import load_dotenv

def scrape_billboard_hot_song_titles(n=10):
    response = requests.get("https://www.billboard.com/charts/hot-100/")

    soup = BeautifulSoup(response.content, 'html.parser')

    song_title_containers = soup.find_all('div', class_="o-chart-results-list-row-container")
    song_titles = []
    for i in range(10):
        song_title = song_title_containers[i].find("ul").find("li", class_="lrv-u-width-100p").find("ul").find("li").find("h3").text.strip()
        song_titles.append(song_title)
    return song_titles

def find_lyric_using_song_title(song_title_param):
    load_dotenv()
    GENIUS_API_ACCESS_TOKEN = os.getenv("GENIUS_API_ACCESS_TOKEN")

    if song_title_param == "":
        return

    song_title = "https://api.genius.com/search?q=" + song_title_param.replace(" ", "%20")

    search_response = requests.get(song_title, headers={'Authorization': f'Bearer {GENIUS_API_ACCESS_TOKEN}'})
    song_api_path = "https://api.genius.com" + search_response.json()["response"]["hits"][0]["result"]["api_path"]
    print("Song API:", song_api_path)
    song_response = requests.get(song_api_path, headers={'Authorization': f'Bearer {GENIUS_API_ACCESS_TOKEN}'})
    lyric_page_path = song_response.json()["response"]["song"]["url"]
    print("Lyric Page:", lyric_page_path)

    lyric_response = requests.get(lyric_page_path)
    soup = BeautifulSoup(lyric_response.content, 'html.parser')
    lyric_container = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1")
    lyric_text = lyric_container.get_text(strip=True, separator="\n")
    return lyric_text