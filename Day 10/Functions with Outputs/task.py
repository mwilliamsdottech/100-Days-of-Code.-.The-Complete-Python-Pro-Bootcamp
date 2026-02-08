def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"You must enter something"

    fname = f_name.title()
    lname = l_name.title()

    return f"{fname} {lname}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
