import useful_functions
import song_scraper

import datetime
import requests
import os

today = datetime.date.today()
song_titles_and_artists = song_scraper.scrape_billboard_hot_song_titles(10)

for i in range(len(song_titles_and_artists)):
    print(i, song_titles_and_artists[i][0], song_titles_and_artists[i][1])
    lyric_text = song_scraper.find_lyric_using_song_title_and_artist(
        song_titles_and_artists[i][0], song_titles_and_artists[i][1])
    #print(lyric_text)

    os.makedirs(f"billboard_hot_songs_{today.strftime('%Y-%m-%d')}", exist_ok=True)
    source_path = f"billboard_hot_songs_{today.strftime('%Y-%m-%d')}/{i+1}_original.txt"
    with open(source_path, 'w', encoding='utf-8') as file:
        file.write(lyric_text)

    dest_path = f"billboard_hot_songs_{today.strftime('%Y-%m-%d')}/{i+1}_translated.txt"

    useful_functions.translate_by_line(source_path, dest_path, 'simple', 5)


    print("----------------------------------------------------")

#useful_functions.translate_by_line(file_path, 'none', 5)




