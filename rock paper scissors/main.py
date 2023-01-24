# import all needed modules;

import random
# define a function to play;


def play():
    # define scores:

    user_score = 0
    computer_score = 0
# three turns!!!

    for i in range(3):
        # let user and computer choice r, p, s, also define scores;

        user = input(
            "what's your choice 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
# tie case;

        if user == computer:
            user_score += 1
            computer_score += 1
            print('tie')
# is win function:

        elif is_win(user, computer):
            user_score += 1
            print('user wins!')
        elif not(is_win(user, computer)):
            computer_score += 1
            print('computer wins!')
# calculate score;
    print(f"user score = {user_score}\n\
computer score = {computer_score}")
# define is win function(r beat s, s beat p, p beat r);


def is_win(player, opponenet):
    # return true if player wins

    if (player == 'r' and opponenet == 's') or (player == 's' and opponenet == 'p')\
            or (player == 'p' and opponenet == 'r'):
        return True
# call play function:


play()
