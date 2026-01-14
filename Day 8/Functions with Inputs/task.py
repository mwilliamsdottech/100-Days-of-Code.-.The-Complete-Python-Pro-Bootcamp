# def greet():
#     print("Hey!")
#     print("How are you?")
#     print("Great to see you!")
#
# greet()
#
# # function that allows input
# def greet_with_name(name):
#     print(f"Hey, {name}")
#     print(f"How are you, {name}")
#     print(f"Great to see you, {name}")
#
# greet_with_name("Mike")

# Functions with multiple inputs
# def greet_with(name, location):
#     print(f"Hey {name}!")
#     print(f"What's it like in {location}?")
#
# greet_with("Michael", "Orlando")

# Functions with multiple inputs using keyword arguments
def greet_with(name, location):
    print(f"Hey {name}!")
    print(f"What's it like in {location}?")

greet_with(name="Michael", location="Orlando")