import requests
from bs4 import BeautifulSoup, NavigableString
import os
from dotenv import load_dotenv
from difflib import SequenceMatcher


# I find that returning song title + artist give a more accurate query for Genius.com
def scrape_billboard_hot_song_titles(n=10):
    response = requests.get("https://www.billboard.com/charts/hot-100/")

    soup = BeautifulSoup(response.content, 'html.parser')

    song_title_containers = soup.find_all('div', class_="o-chart-results-list-row-container")
    song_titles_and_artists = []
    for i in range(n):
        song_title = song_title_containers[i].find("ul").find("li", class_="lrv-u-width-100p").find("ul").find("li").find("h3").text.strip()
        artist = song_title_containers[i].find("ul").find("li", class_="lrv-u-width-100p").find("ul").find("li").find("span").text.strip()
        song_titles_and_artists.append((song_title, artist))
    return song_titles_and_artists



def find_lyric_using_song_title_and_artist(song_title_param, artist_param):
    load_dotenv()
    GENIUS_API_ACCESS_TOKEN = os.getenv("GENIUS_API_ACCESS_TOKEN")

    if song_title_param == "":
        return

    search_query = "https://api.genius.com/search?q=" + song_title_param.replace(" ", "%20") + "%20" + artist_param.replace(" ", "%20")

    search_response = requests.get(search_query, headers={'Authorization': f'Bearer {GENIUS_API_ACCESS_TOKEN}'})

    # Check likelihood that search query result is from same artist
    # Stop at 80% likelihood
    hits = search_response.json()["response"]["hits"]
    song_api_path = ""
    lyric_page_path = ""
    for i in hits:
        hit_artist = i["result"]["artist_names"]
        print("Matching sequence", hit_artist, artist_param)
        print("Ratio: ", SequenceMatcher(None, hit_artist, artist_param).ratio())
        #print("Inverse Ratio: ", SequenceMatcher(None, artist_param, hit_artist).ratio())
        if SequenceMatcher(None, hit_artist, artist_param).ratio() > 0.8:
            song_api_path = "https://api.genius.com" + i["result"]["api_path"]
            lyric_page_path = i["result"]["url"]
            break

    print("Song API:", song_api_path)
    print("Lyric Page:", lyric_page_path)

    lyric_response = requests.get(lyric_page_path)
    soup = BeautifulSoup(lyric_response.content, 'html.parser')
    lyric_containers = soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-1")
    lyric_text = ""
    for i in lyric_containers:
        lyric_text += i.get_text(strip=True, separator="\n") + "\n"
    return lyric_text