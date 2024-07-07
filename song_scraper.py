import requests
from bs4 import BeautifulSoup

def scrape_billboard_hot_song_titles(n=10):
    response = requests.get("https://www.billboard.com/charts/hot-100/")

    soup = BeautifulSoup(response.content, 'html.parser')

    song_title_containers = soup.find_all('div', class_="o-chart-results-list-row-container")
    song_titles = []
    for i in range(10):
        song_title = song_title_containers[i].find("ul").find("li", class_="lrv-u-width-100p").find("ul").find("li").find("h3").text.strip()
        song_titles.append(song_title)
    return song_titles