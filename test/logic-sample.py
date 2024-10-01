# Simple script to test python

# Section 1: Demo output
print("Output Demo: Hello World!")

# ----------------------------------------
# Section 2: For loop to demonstrate loops
print("\nFor loop demonstration:")
for i in range(5):
    print(f"Loop iteration {i}")

# ----------------------------------------
# Section 3: Getting input from the user and convert to int if needed
print("\nUser input demonstration:")
user_input = int(input("Enter a number between 0-10: "))

# ----------------------------------------
# Section 4: Control structure with a nested if statement
print("\nControl structure demonstration:")

if 0 <= user_input <= 10:
    if user_input > 5:
        print(f"{user_input} is greater than 5")
    elif user_input == 5:
        print(f"{user_input} is equal to 5")
    else:
        print(f"{user_input} is not greater than 5")
else:
    print("The number is out of the specified range.")

