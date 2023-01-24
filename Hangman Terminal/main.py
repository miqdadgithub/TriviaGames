# import all needed modules;
import random
from random_word import words
import string
from hangman_visual import lives_visual_dict
# not all words are valid to guess(since spaces...);


def get_valid(words):
    # choice a random word from words;
    word = random.choice(words)
# keep looping till find a word with no ' ' or '-';
    while '-' in word or ' ' in word:
        word = random.choice(words)
# return a word with not ' ' or '-';
    return word.upper()
# define a function to keep track of letters we've guesses and which is correct;


def hangman():
    word = get_valid(words)
# keep all letters in word in a set, and a set of upper case english letters from string module;
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
# define the lives of the man;
    lives = 7
# loop through till they guess it correct;
    while len(word_letters) > 0 and lives > 0:
        # tell user what are used letter are and live remained;
        # .join() concate the list and spearate by what is before . which is space here.
        print("you have used these letters: ", ' '.join(used_letters))
        print(f"your reaming lives are = {lives}")
# tell the user what is current is with - for unguessed  letters;
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ''.join(word_list))
# get user guess;
        user_letter = input('enter a letter: ').upper()
# if this is valid letter and haven't been used yet;
        if user_letter in (alphabet - used_letters):
            # added to used_letters set;
            used_letters.add(user_letter)
# remove it from word_letters set;
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(lives_visual_dict[lives])
# if it's already used tell the user;
        elif user_letter in used_letters:
            print(f'you have already used {user_letter}')
# invalid input;
        else:
            print('invalid input')
# you have lost and the word is;
    if lives == 0:
        print(f"Ohh you've lost, the word is {word}")
# you win and the word;
    else:
        print(f"great you've won!, the word is {word}")


# run the function in the main module;
if __name__ == "__main__":
    hangman()
