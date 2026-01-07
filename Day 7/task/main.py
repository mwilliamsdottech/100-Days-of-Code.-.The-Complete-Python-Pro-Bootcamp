import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
guesses_remaining = 5
while guesses_remaining > 0:
    guess = input("\nGuess a letter: ").lower()

    if guess in chosen_word:

        # TODO-2: Change the for loop so that you keep the previous correct letters in display.
        display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
            else:
                display += "_"
        print(display)
    else:
        guesses_remaining -= 1
        if guesses_remaining > 1:
            print(f"Try again. {guesses_remaining} guesses remaining.")
        else:
            print(f"Try again. {guesses_remaining} guess remaining.")

else:
    print("\nGame Over.")