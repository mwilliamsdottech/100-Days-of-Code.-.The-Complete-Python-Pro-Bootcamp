# Receive pizza order and toppings
# Provide total price

# Pizza prices by size
sm = 15
med = 20
lrg = 25

# Toppings prices
add_pepperoni_sm = 2
add_pepperoni_med_lrg = 3
add_cheese = 1

total_cost = 0

print("\nWelcome to Python Pizza Deliveries! \n")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Get the size and add price accordingly
if size == "S":
    total_cost += sm
elif size == "M":
    total_cost += med
elif size == "L":
    total_cost += lrg
else:
    print("You must type S, M, or L!")


# If the patron wants pepperoni, check to see what size pizza they ordered
# And add the appropriate price. If they chose S, add $2. Otherwise, add $3
if pepperoni == "Y":
    if size == "S":
        total_cost += add_pepperoni_sm
    else:
        total_cost += add_pepperoni_med_lrg

# If patron wants extra cheese add the cost
if extra_cheese == "Y":
    total_cost += add_cheese

# Display the total cost
print(f"\nYour final bill is ${total_cost}")