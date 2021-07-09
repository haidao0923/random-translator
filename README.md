# random-translator
Translate given text into every languages recognized by Google Translator and then back into English.
The order of the languages passed in is randomized which can lead to new and interesting results every time

Inspired by a youtube video of "Let It Go" being translated to multiple languages and back into english https://www.youtube.com/watch?v=2bVAoVlFYf0

Interesting Note: While doing this project, I discovered that translating by line is often better than translating the entire text (which is why I added a second function to translate by line). This did not seem obvious at first, but it made sense since translating large chunks of text could result in Google Translate attempting to combine multiple words resultings in an entirely different meaning.
