import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?  "))
nr_symbols = int(input(f"How many symbols would you like?  "))
nr_numbers = int(input(f"How many numbers would you like?  "))

holder = []

for letter in range(1,nr_letters +1):
    holder.append(random.choice(letters))

for symbol in range(1,nr_symbols +1):
    holder.append(random.choice(symbols))

for number in range(1,nr_numbers +1):
    holder.append(random.choice(numbers))

random.shuffle(holder)

password = ""

for char in holder:
    password += char

print(f"\nYour password is: {password}")