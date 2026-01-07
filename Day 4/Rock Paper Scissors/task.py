import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

characters = [rock, paper, scissors]
computer_choice = random.randint(0,2)

user_input = int(input("\nLet's play Rock, Paper, Scissors!\n0: Rock\n1: Paper\n2: Scissors\n\nEnter your choice: "))

if user_input == "":
    print("You must enter 0, 1, or 2")
else:
    if user_input >= 0 and user_input <= 2:
        print("\nYou played:")
        print(characters[user_input])

        print("Computer played:")
        print(characters[computer_choice])

        if computer_choice != user_input:
            if computer_choice > user_input:
                print("You lose.")
            elif user_input == 2 and computer_choice == 0:
                print("You lose.")
            elif user_input > computer_choice:
                print("You win!")
        elif computer_choice == 2 and user_input == 0:
                    print("You win!")
        else:
            print("You tied.")
    else:
        print("You've entered an invalid character. Try again.")
