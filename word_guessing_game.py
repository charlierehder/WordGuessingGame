import random

word_filename = "words.txt"

def get_word():

    with open(word_filename, "r") as word_file:
        return random.choice(word_file.readlines()).strip()

