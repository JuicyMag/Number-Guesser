import random
#Number guesser is a game where a random number is selected and the player has to guess the right number in less than X guesses


#starting number of guesses a user has
number_of_guesses = 5
turn_number = 0

#all information for random number generation; upper and lower bounds
random_num_range_min = 1
random_num_range_max = 200
random_num = random.randint(random_num_range_min, random_num_range_max)
print(random_num)



while number_of_guesses > 0:
    turn_number= 1
    guess = int(input("What number would you like to guess?"))

    #With the difference I want to be able to give hints. I can detect how far the guess is off (by the difference) and give hints accordingly
    difference = abs(guess - random_num)
    


    if difference > 50:
        print("You're at least 50 numbers off!")
    elif difference < 50 and difference >20:
        print("You're between 20 and 50 numbers away! But still wrong!")
    elif difference < 20:
        print("You're less than 20 numbers away! But still wrong!")
    if guess != random_num and turn_number == 1:
        number_of_guesses = number_of_guesses -1
        print(f'TESTESTETESTIncorrect guess. Remaining guesses:', number_of_guesses)
        turn_number = turn_number + 1

    elif guess != random_num:
        number_of_guesses = number_of_guesses - 1
        print(f'Incorrect guess. Remaining guesses:', number_of_guesses)


    else:
        print("GAME WON: Holy shit you aren't a nerd you WON")
        number_of_guesses = -1
#not happy with having to specific guesses = 0 but was getting issues with game winning guess printing win message and no more guesses message
if number_of_guesses == 0:
    print("You ran out of guesses, game over NERD")

