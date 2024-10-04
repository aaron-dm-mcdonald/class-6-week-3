# sample/functions-sample.py
# Simple Python script to demonstrate functions
#------------------------------------------------------------------

# Function to greet a user
def greet(name):
  
    # This function greets the person passed in as a parameter.

    # Print a greeting message
    print(f"Hello, {name}!")

#------------------------------------------------------------------


# Function to add two numbers
def add_numbers(a, b):
   
    # This function returns the sum of two numbers.
    
    # Calculate the sum of a and b
    return a + b

#------------------------------------------------------------------


# Function with a default argument
def describe_pet(pet_name, animal_type='dog'):
 
    # Print the type of animal
    print(f"\nI have a {animal_type}.")
    # Print the pet's name
    print(f"My {animal_type}'s name is {pet_name}.")

#------------------------------------------------------------------

# Function using *args to accept multiple arguments
def print_fruits(*fruits):
    """
    This function prints all the fruits passed as arguments.
    """
    # Print a header
    print("Fruits:")
    # Loop through each fruit in the arguments and print it
    for fruit in fruits:
        print(f"- {fruit}")

# Calling the functions
# Greet a user named Alice
greet("Alice")

# Calculate and print the sum of 5 and 3
print(f"Sum: {add_numbers(5, 3)}")

# Describe a pet named Buddy, which is a dog by default
describe_pet("Buddy")

# Describe a pet named Whiskers, which is a cat
describe_pet("Whiskers", "cat")

# Print a list of fruits
print_fruits("Apple", "Banana", "Cherry")
