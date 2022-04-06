import random

# helper function to get random words from dictionary
def get_word():
    word_filename = "words.txt"
    with open(word_filename, "r") as word_file:
        return random.choice(word_file.readlines()).strip()


# setup gameplay loop by getting a random word
# and setting up a display string
correct_word = get_word()
display = ["_"] * len(correct_word)
turn_limit = 7

for i in range(turn_limit):

    guess = str(input("Guess: "))
    

    # single letter guess
    if len(guess) == 1:
        for i,v in enumerate(correct_word):
            if v == guess:
                display[i] = v
        print("".join(display))

    # guess full word
    else:
        if guess == correct_word:
            print("You win!")
            break

