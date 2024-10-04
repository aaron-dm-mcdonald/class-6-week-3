# sample/functions-sample.py
# Simple Python script to demonstrate functions
#------------------------------------------------------------------

# Function to greet a user
def greet(name):
  
    # This function gets its argument by passing it in as a parameter.

    # Print a greeting message
    print(f"Hello, {name}!")

#------------------------------------------------------------------


# Function to add two numbers
def add_numbers(a, b):
   
    # This function has a return value.
    c = a + b
    # Calculate the sum of a and b
    return c

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
   
    # This function prints all the fruits passed as arguments.
   
    # Print a header
    print("Fruits:")
    # Loop through each fruit in the arguments and print it
    for fruit in fruits:
        print(f"- {fruit}")

#------------------------------------------------------------------

# Calling the functions

# Passes the argument "Alice" as a parameter
greet("Alice")

# Pass a=b, b=3 as parameters with return value
print(f"Sum: {add_numbers(5, 3)}")

# Describe a pet, with a default value
describe_pet("Buddy")

# Describe a pet named which overrides the default value 
describe_pet("Whiskers", "cat")

# Print a list of fruits with muliple arguments being passed to the same parameter
print_fruits("Apple", "Banana", "Cherry")
