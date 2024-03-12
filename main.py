# we guess the number, the computer says whether we went too high, too low or it is the correct number

import random       # random package to access randint function

def guess(x):
    random_number = random.randint(1,x)     # randit function to randomly select a number between a range
    guess = 0
    # looping through the options until we get the right answer hence Loop
    # while loop -  we don't have pre defined universe to iterate over

    while guess != random_number:
        guess =int(input(f"Guess a number between 1 and {x}: "))
        #print(guess)
        if guess < random_number:
            print("Sorry, guess again, Too Low.")
        elif guess > random_number:
            print("Sorry, guess again, Too High.")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly. ")
guess(10)