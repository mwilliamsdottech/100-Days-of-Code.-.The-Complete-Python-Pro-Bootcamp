print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")

move = input("\nWhich direction would you like to go? Left or Right? \nType L or R: ")
move = move.lower()

if move != "l" or move != "left":
    print("\nYou fell into a hole. Game Over.")
else:
    move = input("\nYou have reached a lake. Would you like to Swim or Wait for a ferry?\nType S or W: ")
    move = move.lower()

    if move != "w":
      print("\nYou were attacked by a trout! Game Over.")
    else:
        move = input("\nGood job. The ferry brought you across "
                     "the lake, and you made it into the house! \n\nThere are 3 doors: Red, Yellow, and Blue. Choose one.\nType R, Y, or B: ")
        move = move.lower()

        if move != "y":
            if move == "r":
                print("\nYou were burned by fire. Game Over.")
            if move == "b":
                print("\nYou were eaten by beasts. Game Over. ")
        else:
            print("\nCongratulations! You found the treasure!")