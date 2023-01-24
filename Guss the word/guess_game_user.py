# games rules;

import random
print('''
the user will guess a random integer between 1 and x(define by player):
>>>>>>>too heigh === the returned value if above the secret number.
>>>>>>>too low === the returned value if below the secret number.
>>>>>>>anything else will indicate the correct value!
''')
# import all needed modules;

# define a function to let the computer to guess the secrete number;


def guess_computer(x):
    # define initial guess;

    guess = 0
# define an upper and lower band to guess in between;

    low = 1
    heigh = x
# while loop to guess till it guess it correctly;

    while True:
        # guess an integer between lower and upper band;

        guess = random.randint(low, heigh)
# ask if it's correct;

        guess_feedback = input(f"is {guess} correct: ")
# use conditionals to decide;

        if guess_feedback.lower() == "too heigh":
            heigh = guess
        elif guess_feedback.lower() == "too low":
            low = guess
        else:
            print(f"yey, I knew it's {guess}")
            break
# call guess function;


guess_computer(10)
