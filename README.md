# random-translator
Translate given text into a subset of every languages recognized by Google Translator and then back into English.
The order of the languages passed in is randomized which can lead to new and interesting results every time.

Inspired by a YouTube video of "Let It Go" being translated to multiple languages and back into english https://www.youtube.com/watch?v=2bVAoVlFYf0

Interesting Note: While doing this project, I discovered that translating by line is often better than translating the entire text (which is why I added a second function to translate by line). This did not seem obvious at first, but it made sense since translating large chunks of text could result in Google Translate attempting to combine multiple words resultings in an entirely different meaning.

## Edit: 3 years later 
I made some huge improvement to this code with scraping songs from Billboard Hot 100 -> integrating Genius API + some (pseudo-illegal :P) hacking + difflib (selecting the top query with high confidence ratio among all matched song queries) -> Github Workflow (coming soon)

I initially thought to use translate entire file for speed but quickly discovered that there is a 5000 character limit so I opted to translate by line again.
Translating by line have its own challenges (illegally scraping lyrics data meant I needed to do some post-cleaning, which resulted in some invalid characters that I had to catch)

![image](https://github.com/haidao0923/random-translator/assets/67529758/12007b46-9739-4c45-af50-8d394f2119e4)
