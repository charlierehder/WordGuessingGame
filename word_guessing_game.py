import random

# helper function to get random words from dictionary
def get_word():
    word_filename = "words.txt"
    with open(word_filename, "r") as word_file:
        return random.choice(word_file.readlines()).strip()

used_words = set()
win_count = 0
loss_count = 0

game_running = True
while(game_running):

    # setup gameplay loop by getting a random word
    # and setting up a display string
    correct_word = get_word()
    while(correct_word in used_words):
        correct_word = get_word()

    display = ["_"] * len(correct_word)
    turn_limit = 7
    print("".join(display))

    turn_number = 0
    while (turn_number < turn_limit):
        
        print("You have 7 guesses")

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
                win_count += 1
                break
            elif guess != correct_word and turn_number != 5:
                turn_number += 1

        print("".join(display))

    if turn_number == turn_limit:
        print("You lost")
        print(f"The correct word was {correct_word}")
        loss_count += 1

    print("---------------------------")
    print(f"| Wins: {str(win_count).zfill(3)} | Losses: {str(loss_count).zfill(3)} |")
    print("---------------------------")

    # ask if player wants to play again
    while(1):
        response = str(input("Do you want to play again? (y/n): "))
        if response == "n":
            game_running = False
            break
        elif response == "y":
            game_running = True # here for redundancy's sake
            break
        else:
            print("Please anwser either 'y' or 'n'")
    
