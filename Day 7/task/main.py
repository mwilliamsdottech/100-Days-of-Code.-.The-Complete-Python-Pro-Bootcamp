import random

def game_over():
    print('''
██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
''')
    print(f"\nThe word was {chosen_word}\nTry again?")

def win_msg():
    print('''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
''')
    phrases = [
    "You guessed it! Nicely done!",
    "That’s it—you got it!",
    "You nailed the word!",
    "Yes! That was the word!",
    "Correct! You did it!",
    "That’s the one—great job!",
    "You found it! Well played!",
    "Bingo! That’s the word!",
    "You got the answer!",
    "Right on! You guessed it!",
    "Fantastic! You cracked it!",
    "Spot on! That’s the word!",
    "Amazing! You got it right!",
    "Perfect! That was it!",
    "Woohoo! You guessed correctly!",
    "Bravo! That’s the word!",
    "Excellent! You found it!",
    "Yes! You got it spot-on!",
    "Impressive! You nailed it!",
    "Hooray! That’s the right word!"
]
    print(random.choice(phrases))

hard_word_list = [
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

med_word_list = [
    "ELEPHANT",
    "GIRAFFE",
    "KANGAROO",
    "DOLPHIN",
    "LEOPARD",
    "CHEETAH",
    "PENGUIN",
    "OSTRICH",
    "PEACOCK",
    "RACCOON",
    "SQUIRREL",
    "RABBIT",
    "TURTLE",
    "OCTOPUS",
    "BUTTERFLY",
    "LADYBUG",
    "BEETLE",
    "WALRUS",
    "PANTHER",
    "JAGUAR",
    "COUGAR",
    "MANATEE",
    "BUFFALO",
    "CAMEL",
    "ZEBRA",
    "FERRET",
    "MEERKAT",
    "MOOSE",
    "IGUANA",
    "TOUCAN",
    "LOBSTER",
    "CRABBY",
    "HERON",
    "STORK",
    "ELK",
    "LYNX",
    "GAZELLE",
    "TAPIR",
    "MARMOT",
    "OTTER",
    "DONKEY",
    "MONKEY",
    "HORSE",
    "PIGEON",
    "RABBIT",
    "TURKEY",
    "CAMEL",
    "LAMB",
    "GOOSE"
]

easy_word_list = [
    "CAT",
    "DOG",
    "COW",
    "PIG",
    "HEN",
    "BAT",
    "FOX",
    "APE",
    "BEE",
    "OWL",
    "RAT",
    "LAMB",
    "DUCK",
    "MULE",
    "FROG",
    "TOAD",
    "SEAL",
    "PONY",
    "CROW",
    "LION",
    "BEAR",
    "GOAT",
    "DEER",
    "SWAN",
    "MOTH",
    "CRAB",
    "TUNA",
    "FISH",
    "DUCK",
    "ANT",
    "BAT",
]

print(
'''
██╗    ██╗ ██████╗ ██████╗ ██████╗        
██║    ██║██╔═══██╗██╔══██╗██╔══██╗       
██║ █╗ ██║██║   ██║██████╔╝██║  ██║       
██║███╗██║██║   ██║██╔══██╗██║  ██║       
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝       
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝        
 ██████╗ ██╗   ██╗███████╗███████╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
╚██████╔╝╚██████╔╝███████╗███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
     CATEGORY: ANIMALS & BUGS                       
''')

level_choice = input("Please choose a level:"
      "\n1. Easy"
      "\n2. Medium"
      "\n3. Hard"
        "\n\n1, 2, or 3? ")
print("\n")

if level_choice == "3":
        chosen_word = random.choice(hard_word_list)
        placeholder = ""
        word_length = len(chosen_word)
        for position in range(word_length):
            placeholder += "_"
        print(f"The word is: {placeholder}")

        guesses_remaining = 6
        correct_letters = []

        while guesses_remaining > 0:
            guess = input("Guess a letter: ").upper()

            display = ""

            if guess in chosen_word:
                for letter in chosen_word:
                    if letter == guess:
                        display += letter
                        correct_letters.append(guess)
                    elif letter in correct_letters:
                        display += letter
                    else:
                        display += "_"
                print(f"\n{display}")

                if "_" not in display:
                     win_msg()
                     break
            else:
                guesses_remaining -= 1
                if guesses_remaining > 1:
                    print(f"\nTry again. {guesses_remaining} guesses remaining.")
                elif guesses_remaining == 1:
                    print(f"\nTry again. {guesses_remaining} guess remaining.")
                elif guesses_remaining == 0:
                    game_over()
                    break
        else:
            game_over()
elif level_choice == "2":
    chosen_word = random.choice(med_word_list)
    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print(f"The word is: {placeholder}")

    guesses_remaining = 6
    correct_letters = []

    while guesses_remaining > 0:
        guess = input("Guess a letter: ").upper()

        display = ""

        if guess in chosen_word:
            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    correct_letters.append(guess)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"
            print(f"\n{display}")

            if "_" not in display:
                win_msg()
                break
        else:
            guesses_remaining -= 1
            if guesses_remaining > 1:
                print(f"\nTry again. {guesses_remaining} guesses remaining.")
            elif guesses_remaining == 1:
                print(f"\nTry again. {guesses_remaining} guess remaining.")
            elif guesses_remaining == 0:
                game_over()
                break
    else:
        game_over()
else:
    chosen_word = random.choice(easy_word_list)
    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print(f"The word is: {placeholder}")

    guesses_remaining = 6
    correct_letters = []

    while guesses_remaining > 0:
        guess = input("Guess a letter: ").upper()

        display = ""

        if guess in chosen_word:
            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    correct_letters.append(guess)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"
            print(f"\n{display}")

            if "_" not in display:
                win_msg()
                break
        else:
            guesses_remaining -= 1
            if guesses_remaining > 1:
                print(f"\nTry again. {guesses_remaining} guesses remaining.")
            elif guesses_remaining == 1:
                print(f"\nTry again. {guesses_remaining} guess remaining.")
            elif guesses_remaining == 0:
                game_over()
                break
    else:
        game_over()