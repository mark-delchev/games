import nltk
nltk.download('words')
from nltk.corpus import words
wordlist = set(words.words())

def is_real_word(word):
    return word.lower() in wordlist


last_letter = "a"

for i in range(5):
    word = input()
    if word[0] == last_letter and is_real_word(word):
        print("Correct!")
        last_letter = word[-1]
