#import random;
import random

# defing several madlibs;

# -----------------computer science--------------------------


def computer_science():
    body_part = input("Body Part: ")
    verb = input("Verb: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    adj5 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    noun_plural_2 = input("Noun (plural): ")

    madlib = f"I love computer programming because it's {adj1}! The journey to becoming a \
good programmer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun_plural_1}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj2} hacker. Knowledge of programming \
lets you take control of your {noun1}. You can create your own personal {noun_plural_2}, anything \
from developing {adj3} software to analyzing data and making predictions about the {noun2}. You can \
maybe even recreate Jarvis and make him extra {adj4}. I hope you'll start your {adj5} journey by \
coding with Kylie :)"

    print(madlib)
# -----------------------harry potter------------------------------


def harry_potter():
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")
    noun6 = input("Noun: ")
    noun_plural = input("Noun plural: ")
    body_part = input("Body part: ")
    body_part2 = input("Body part: ")
    verb = input("Verb: ")
    verb_past = input("Verb (past tense): ")
    verb_past2 = input("Verb (past tense): ")
    spell1 = input("Spell: ")
    spell2 = input("Spell: ")

    madlib = f"A {adj1} glow burst suddenly across the enchanted sky above them as an edge of \
dazzling sun appeared over the sill of the nearest {noun1}. The light hit both of their {body_part} \
at the same time, so that Voldemort’s was suddenly a flaming {noun2}. Harry heard the high voice \
shriek as he too {verb_past} his best hope to the heavens, pointing Draco’s {noun3}:\n\
\"{spell1}!\"\n\
\"{spell2}!\"\n\
The bang was like a cannon blast, and the {adj2} flames that erupted between them, \
at the dead center of the circle they had been treading, marked the point where the \
{noun_plural} collided. Harry saw Voldemort’s {adj3} jet meet his own spell, saw the Elder Wand \
fly high, dark against the sunrise, spinning across the enchanted ceiling like the \
head of Nagini, spinning through the air toward the master it would not {verb}, who had \
come to take full possession of it at last. And Harry, with the unerring skill of a Seeker, \
caught the {noun4} in his free hand as Voldemort fell backward, arms splayed, the slit pupils \
of the {adj4} {body_part2} rolling upward. Tom Riddle hit the floor with a mundane finality, his body \
feeble and shrunken, the white hands empty, the snakelike face vacant and unknowing. Voldemort \
was dead, {verb_past2} by his own rebounding {noun5}, and Harry stood with two wands in his hands, \
staring down at his enemy’s {noun6}."

    print(madlib)
# -----------------hunger games--------------------------


def hunger_games():
    number = input("Number: ")
    adj = input("Adjective: ")
    verb = input("Verb: ")
    verb2 = input("Verb: ")
    noun = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")
    noun_plural = input("Noun (plural): ")
    noun_plural_2 = input("Noun (plural): ")
    noun_plural_3 = input("Noun (plural): ")
    sound_important = input("Name of something that sounds important: ")

    madlib = f"{number} seconds. That’s how long we’re required to {verb} on our metal circles before \
the sound of a {noun} releases us. Step off before the {number} seconds is up, and {noun_plural} blow your \
legs off. {number} seconds to take in the ring of tributes all equidistant from the {sound_important}, a giant \
{adj} {noun2} shaped like a {noun3} with a curved tail, the mouth of which is at least twenty feet \
high, spilling over with the things that will give us life here in the arena. Food, containers of water, \
{noun_plural_2}, medicine, garments, {noun_plural_3}. Strewn around the {sound_important} are other supplies, their value \
decreasing the farther they are from the {noun2}. For instance, only a few steps from my feet lies a three-foot \
square of {noun4}. Certainly it could be of some use in a downpour. But there in the mouth, I can see a {noun5} \
that would protect from almost any sort of weather. If I had the guts to go in and {verb2} for it against \
the other twenty-three tributes. Which I have been instructed not to do."

    print(madlib)
# -----------------------zombie--------------------------


def zombie():
    time_of_day = input("Time of Day: ")
    body_part_plural = input("Body Part (plural): ")
    color = input("Color: ")
    verb_past_tense = input("Verb (past tense): ")
    food = input("Food: ")
    noun1 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")

    madlib = f"It was a {adj1} summer {time_of_day} when we realized that the vaccine to stop \
spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for {body_part_plural} \
and the streets were lined with these monsters holding {noun_plural_1} in their hands. \
Their eyes were {color} with hunger as they {verb_past_tense} around the city looking for {food}. \
They were {adj2} and {adj3}, unknowing how to act in this human world... except eat {body_part_plural}!!!! \
That was their sole mission and they were dedicated towards achieving it for the sake of {noun1}."

    print(madlib)


# create a list of the madlib functions;
madlib_list = ["computer_science()", "harry_potter()",
               "hunger_games()", "zombie()"]

# choice a madlib;
madlib_choice = random.choice(madlib_list)

# use conditional to run a function;
if madlib_choice == "computer_science()":
    computer_science()
elif madlib_choice == "harry_potter()":
    harry_potter()
elif madlib_choice == "hunger_games()":
    hunger_games()
elif madlib_choice == "zombie()":
    zombie()
