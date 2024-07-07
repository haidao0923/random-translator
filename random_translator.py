import useful_functions
import song_scraper

song_titles = song_scraper.scrape_billboard_hot_song_titles()

for i in range(len(song_titles)):
    print(i, song_titles[i])

file_path = 'text.txt'

#useful_functions.translate_by_line(file_path, 'none', 5)
#useful_functions.translate_entire_file(file_path, 'simple', 5)




