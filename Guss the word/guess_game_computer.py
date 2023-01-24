# import all needed modules;

import random
# define a function to make a guess between 1 - x;


def guess(x):
    right_guess = random.randint(1, x)
# create a while loop to loop till the user guessed correctly;

    guess = 0
    while guess != right_guess:
        guess = int(input(f"Enter a guess between 1 and {x}: "))
# use conditionals to make it more interactive;

        if guess < right_guess:
            print(f"{guess} is too low!")
        elif guess > right_guess:
            print(f"{guess} is too heigh!")

    print(f"Yey. you have guess {guess} correctly!")


# call the guess function;
guess(10)
