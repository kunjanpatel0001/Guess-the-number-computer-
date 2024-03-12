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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
     #randint:- gives error whe low and high are the same hence if else condition
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)  
        else:
            guess = low     # could also be high bcz low = high   
        feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)?").lower()        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay...the computer guesses your number {guess}, correctly.") 
# computer_guess(1000)
    guess(100)