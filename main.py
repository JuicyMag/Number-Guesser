import random
#Number guesser is a game where a random number is selected and the player has to guess the right number in less than X guesses


#starting number of guesses a user has
number_of_guesses = 5

#all information for random number generation; upper and lower bounds
random_num_range_min = 1
random_num_range_max = 200
random_num = random.randint(random_num_range_min, random_num_range_max)
print(random_num)

while number_of_guesses > 0:
    # turn = 1
    # while turn == 1:
    # guess = int(input("A random number between " + str(random_num_range_min) + " and " + str(random_num_range_max) + " has just been selected. What is your guess?"))

    guess = int(input("What is your guess?"))

    if guess != random_num:
        number_of_guesses = number_of_guesses -1
        print(f'Remaining guesses:', number_of_guesses)


    else:
        print("GAME WON: Holy shit you aren't a nerd you WON")
        number_of_guesses = -1

#not happy with having to specific guesses = 0 but was getting issues with game winning guess printing win message and no more guesses message
if number_of_guesses == 0:
    print("You ran out of guesses, game over NERD")
