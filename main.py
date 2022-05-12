import random


def run_game():
    """This function starts the game text"""

    print("I am thinking of a three digit number. Try to guess what it is.\nHere are some clues.\n"
         "When I say Pico: That means one digit is correct but in the wrong place\n"
          "When I say Femi: That means one digit is correct and in the right place\n"
          "When I say Bagels: No digit is correct\n"
          "I have thought of a number.\nYou have 10 guesses to get it.")
    play_game()


def check_num(guess, b_num):
    """This checkes the users guess and compares it to the random number"""

    guess = str(guess)
    b_num = str(b_num)
    clues = []
    for i in range(len(guess)):
        if guess[i] == b_num[i]:
            clues.append("Femi")
        elif guess[i] in b_num:
            clues.append("Pico")
    if len(clues) == 0:
        return print("Bagels")
    else:
        return print(" ".join(clues))


def play_game():
    bagel_num = random.randint(100, 1000)
    # print(bagel_num) Used to test generated number
    guess_num = 0
    game_is_running = True
    while game_is_running:
        user_guess = input(f"Guess #{guess_num + 1}: ")
        while True:
            if user_guess.isalpha() or user_guess == "" or int(user_guess) < 100 or int(user_guess) > 999:
                user_guess = input("Invalid: ")
            else:
                user_guess = int(user_guess)
                break
        if user_guess == bagel_num:
            print("You Win!")
            break
        check_num(user_guess, bagel_num)
        guess_num += 1
        if guess_num >= 10:
            print(f"You lose! The number was {bagel_num}.")
            game_is_running = False


run_game()
play_again = input("Would you like to play again? Y or N ").upper()
if play_again == "Y":
    run_game()
else:
    print("Good Bye!")

