import random

# helper function to get random words from dictionary
def get_word():
    word_filename = "words.txt"
    with open(word_filename, "r") as word_file:
        return random.choice(word_file.readlines()).strip()

# define set to store words that have been used in previous games
used_words = set()

# define win and loss counts to display
win_count = 0
loss_count = 0

# system loop
game_running = True
while(game_running):

    # setup gameplay loop by getting a random word
    # and setting up a display string
    correct_word = get_word()
    while(correct_word in used_words):
        correct_word = get_word()

    # create 'blank' string to display as game progresses
    display = ["_"] * len(correct_word)

    # set turn limit and display blank string
    turn_limit = 7
    print("".join(display))


    print("Words are case sensitive and can contain apostrophes")
    print("You have 7 guesses")

    # game loop
    turn_number = 0
    while (turn_number < turn_limit):
        

        # get user input
        guess = str(input(f"You have {turn_limit - turn_number}/7 lives left: "))

        lose_life = True

        # single letter guess
        if len(guess) == 1:
            for i,v in enumerate(correct_word):
                if v == guess:
                    lose_life = False
                    display[i] = v

        # guess full word
        else:
            if guess == correct_word:
                print("You win!")
                win_count += 1
                break

        if lose_life: 
            turn_number += 1

        print("".join(display))

    # print loss message and increment loss counter
    if turn_number == turn_limit:
        print("You lost")
        print(f"The correct word was {correct_word}")
        loss_count += 1

    # display win/loss record
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
    
