import random

def game_over():
    print("\nGame Over. Try again?")

def win_msg():
    phrases = ["\nYou won!", "\nYou're awesome!", "\nYou rock!", "\nAmazing!", "\nCool!", "\nFantastic!", "\nPhenomenal!", "\nWoo Hoo!"]
    print(random.choice(phrases))

word_list = [
    "ANTELOPE",
    "BUFFALO",
    "CARIBOU",
    "COYOTE",
    "BADGER",
    "FERRET",
    "MEERKAT",
    "OTTER",
    "MONGOOSE",
    "PORCUPINE",
    "ARMADILLO",
    "HEDGEHOG",
    "WOLVERINE",
    "MARMOT",
    "MUSKRAT",
    "WOODCHUCK",
    "GAZELLE",
    "IBIS",
    "HERON",
    "PUFFIN",
    "CORMORANT",
    "PELICAN",
    "KINGFISHER",
    "ROADRUNNER",
    "TORTOISE",
    "MONITOR",
    "CHAMELEON",
    "GECKO",
    "ANACONDA",
    "PYTHON",
    "COBRA",
    "MANTA",
    "STINGRAY",
    "OCTOPUS",
    "CUTTLEFISH",
    "LOBSTER",
    "CRAYFISH",
    "SCORPION",
    "TARANTULA",
    "CENTIPEDE",
    "MILLIPEDE",
    "BUTTERFLY",
    "DRAGONFLY",
    "GRASSHOPPER",
    "PRAYINGMANTIS",
    "CATERPILLAR",
    "SALAMANDER",
    "NEWT",
    "FIREANT",
    "HORSESHOECRAB"
]


chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# While loop to let the user guess again.
guesses_remaining = 5
correct_letters = []

while guesses_remaining > 0:
    guess = input("Guess a letter: ").upper()
    display = ""
    if guess in chosen_word:
        #Keep the previous correct letters on display.
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
                print(f"\n{display}")
            elif letter in correct_letters:
                display += letter
                print(f"\n{display}")
            else:
                display += "_"

        # if "_" not in display:
        #     win_msg()
        #     break
    else:
        guesses_remaining -= 1
        if guesses_remaining > 0:
            print(f"\nTry again. {guesses_remaining} guesses remaining.")
        elif guesses_remaining == 1:
            print(f"\nTry again. {guesses_remaining} guess remaining.")
        elif guesses_remaining == 0:
            game_over()
            break
else:
    game_over()