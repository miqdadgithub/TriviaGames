# import all needed modules(note they are all in same directory so just import,
# other wise use from *** import***);
import computer_science
import harry_potter
import hunger_games
import zombie
import random
# this is true if the code is from the 'main' module;
if __name__ == "__main__":
    madlib_file = random.choice(
        [computer_science, harry_potter, hunger_games, zombie])
    madlib_file.madlib()
