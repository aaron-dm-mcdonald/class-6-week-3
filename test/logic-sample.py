# logic-sample.py
# Simple script to test python's basic logical structures 
#------------------------------------------------------------------


# Section 1: Demo output function
# Print a welcome message to demonstrate basic output functionality.
print("Output Demo: Hello World!")


# ----------------------------------------
# Section 2: Getting input from the user for the loop range
# Print a message indicating the start of user input demonstration.
print("\nUser input demonstration:")
# Prompt the user to enter a number between 0 and 10.
user_input = int(input("Enter a number between 0-10: "))


# ----------------------------------------
# Section 3: For loop to demonstrate loops using user input
# Print a message indicating the start of the for loop demonstration.
print("\nFor loop demonstration:")
# Use a for loop to iterate through a range of numbers from 0 to the user's input.
for i in range(user_input):
    # Print the current iteration number (i) during each loop.
    print(f"Loop iteration {i}")


# ----------------------------------------
# Section 4: Control structure with a nested if statement
# Print a message indicating the start of the control structure demonstration.
print("\nControl structure demonstration:")

# Check if the user input is within the valid range (0 to 10).
if 0 <= user_input <= 10:
    # If the input is greater than 5, execute this block.
    if user_input > 5:
        # Inform the user that their input is greater than 5.
        print(f"{user_input} is greater than 5")
    # If the input is exactly 5, execute this block.
    elif user_input == 5:
        # Inform the user that their input is equal to 5.
        print(f"{user_input} is equal to 5")
    # If the input is less than 5 (but valid), execute this block.
    else:
        # Inform the user that their input is not greater than 5.
        print(f"{user_input} is not greater than 5")
# If the input is outside the valid range, execute this block.
else:
    # Inform the user that their input is out of the specified range.
    print("The number is out of the specified range.")


