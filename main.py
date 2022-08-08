import random
#Number guesser is a game where a random number is selected and the player has to guess the right number in less than X guesses


#starting number of guesses a user has
number_of_guesses = int(input("How many turns would you like?"))
turn_number = 0

#all information for random number generation; upper and lower bounds
random_num_range_min = int(input("In this game you get to pick the range the number randomly gets generated from. Give me the lower bound. "))
random_num_range_max = int(input("Give me the upper bound. "))
random_num = random.randint(random_num_range_min, random_num_range_max)
# print(random_num)

turn_number = 1

print("A number between " + str(random_num_range_min) + " and " + str(random_num_range_max) + " was just selected.")    



while number_of_guesses > 0:
        
    if turn_number == 1:
        guess = int(input("What number would you like to guess?"))
        # difference = abs(guess - random_num)
        turn_number = turn_number + 1
        
        if guess > random_num_range_max or guess < random_num_range_min:
            print("Your guess is out of the range of the random number! Your turn was not used.")

        else:
               
            if guess != random_num:
                difference = abs(guess - random_num) 
                if difference > 50:
                    print("You're at least 50 numbers off!")

                elif difference < 50 and difference >20:
                    print("You're less than 50 numbers away! But still wrong!")

                elif difference < 20 and difference> 5:
                    print("You're less than 20 numbers away! But still wrong!")

                elif difference < 5:
                    print("You're less than 5 numbers away! But still wrong!")

                number_of_guesses = number_of_guesses -1
                print(f'Incorrect guess. Remaining guesses:', number_of_guesses)
                print("")
                turn_number = turn_number + 1
        

            else:
                print("GAME WON: Holy shit you aren't a nerd you WON")
                number_of_guesses = -1
            turn_number = turn_number + 1
            
    else:
            guess = int(input("What number would you like to guess turn not 1?"))
            difference = abs(guess - random_num)
            
            if guess > random_num_range_max or guess < random_num_range_min:
                print("Your guess is out of the range of the random number! Your turn was not used.")
                
            if guess != random_num:
                if difference > 50:
                    print("You're at least 50 numbers off!")
                elif difference < 50 and difference >20:
                    print("You're less than 50 numbers away! But still wrong!")
                elif difference < 20 and difference> 5:
                    print("You're less than 20 numbers away! But still wrong!")
                elif difference < 5:
                    print("You're less than 5 numbers away! But still wrong!")
                number_of_guesses = number_of_guesses -1
                print(f'Incorrect guess. Remaining guesses:', number_of_guesses)
                print("")
                turn_number = turn_number + 1

            else:
                print("GAME WON: Holy shit you aren't a nerd you WON")
                number_of_guesses = -1
            turn_number = turn_number + 1

if number_of_guesses == 0:
    print("You ran out of guesses, game over NERD")
    print("Your number was: " + random_num)
    print("random test to see if git is working!")