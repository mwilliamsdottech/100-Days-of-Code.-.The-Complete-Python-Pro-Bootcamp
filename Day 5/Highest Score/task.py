student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

sum = 0

print("\nYou entered the following numbers:")
print(f"{student_scores}\n")

# Add up the student scores
for score in student_scores:
    sum += score

# Find the biggest score
max_num = 0
for number in student_scores:
    if number > max_num:
        max_num = number


print(f"Total: {sum}")
print(f"Max #: {max_num}")