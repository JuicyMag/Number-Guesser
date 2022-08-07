from random import *
#Number guesser is a game where a random number is selected and the player has to guess the right number in less than X guesses

#starting number of guesses a user has
number_of_guesses = 5
random_num = 6

guess = int(input("What is your guess?"))
while number_of_guesses > 0:

    if guess != random_num:
        number_of_guesses = number_of_guesses -1
        print(f'Remaining guesses:', number_of_guesses)

    else: #guess == random_num:
        print("Holy shit you aren't a nerd you WON")
        number_of_guesses = -1

if number_of_guesses == 0:
    print("You ran out of guesses, game over NERD")
