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

turn_number = 0
while (turn_number < turn_limit):

    # get user input
    guess = str(input(f"Guess {turn_number + 1}: "))
    

    # single letter guess
    if len(guess) == 1:
        for i,v in enumerate(correct_word):
            if v == guess:
                display[i] = v
        turn_number += 1

    # guess full word
    else:
        if guess == correct_word:
            print("You win!")
            break
        elif guess != correct_word and turn_number != 5:
            turn_number += 1

    print("".join(display))

if turn_number == turn_limit:
    print("You lost")
    print(f"The correct word was {correct_word}")

