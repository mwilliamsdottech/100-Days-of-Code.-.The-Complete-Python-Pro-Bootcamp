# Odd or even check

print("\n*************\nOdd or Even?\n*************")
number = int(input("\nEnter a number please: "))
check_number = number % 2

if check_number == 0:
    print("The number you entered is even")
else:
    print("The number you entered is odd")