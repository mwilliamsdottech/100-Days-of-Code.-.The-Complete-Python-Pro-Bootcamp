print("\n**************\nTIP CALCULATOR\n**************")

bill = float(input("\nWhat was the total bill? $"))
tip = int(input("\nWhat percentage tip would you like to give? 10%, 12%, or 15%? "))

tip_in_decimal_format = tip / 100
total_tip = bill * tip_in_decimal_format

print(f"The tip amount is: $" + str(round(total_tip, 2)))

people = int(input("\nHow many people are splitting the bill? "))

print(f"\nThe total with tip is ${bill + float(round(total_tip))}. \nEach person should chip in $" ,round(total_tip/people,2),"for tip.")
