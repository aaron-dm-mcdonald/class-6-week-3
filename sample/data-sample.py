# data-samples.py
# Illustrates basic python data types, some data structures and their associated behavior. 
#------------------------------------------------------------------


# Variables
# Variables store individual pieces of data.
name = "Alice"  # String variable: a sequence of characters
age = 30        # Integer variable: a whole number
height = 5.5    # Float variable: a number with a decimal point

# Print statements to display variable values
print("Variable - Name:", name)
print("Variable - Age:", age)
print("Variable - Height:", height)


#------------------------------------------------------------------


# Lists
# Lists store ordered collections of items.
fruits = ["apple", "banana", "cherry"]
print("\nList - Fruits:", fruits)
# Accessing elements in a list by index (starting from 0)
print("List - First fruit:", fruits[0])  # First element
print("List - Last fruit:", fruits[2])    # Last element by index
print("List - Last fruit:", fruits[-1])    # Last element using negative indexing (going backwards in the list)


#------------------------------------------------------------------


# Advanced List
# Lists can contain mixed data types and even other lists.
adv_list = ["text", 123, 45.6, [1, 2, 3], {"key": "value"}]
print("\nAdvanced List - Mixed data types:", adv_list)
print("Advanced List - Nested list:", adv_list[3])  # Accessing a nested list
print("Advanced List - Nested list - Single Value:", adv_list[3][1])  # Accessing a value in the nested list
print("Advanced List - Dictionary inside list:", adv_list[4])  # Accessing a dictionary in the list


#------------------------------------------------------------------


# Dictionaries
# Dictionaries store unordered collections of key-value pairs.
person = {
    "name": "Bob",          # Key "name" maps to the value "Bob"
    "age": 25,             # Key "age" maps to the value 25
    "height": 6.0          # Key "height" maps to the value 6.0
}
# Print the entire dictionary
print("\nDictionary - Person:", person)
# Accessing individual values using their corresponding keys
print("Dictionary - Name:", person["name"])  # Accessing value associated with key "name"
print("Dictionary - Age:", person["age"])    # Accessing value associated with key "age"


#------------------------------------------------------------------


# Advanced Dictionary
# Dictionaries can contain nested dictionaries and lists.
adv_dict = {
    "name": "Charlie",                        # Key "name" maps to the value "Charlie"
    "details": {                              # Key "details" maps to another dictionary
        "age": 28,                            # Key "age" in the nested dictionary
        "height": 5.9,                        # Key "height" in the nested dictionary
        "hobbies": ["reading", "cycling", "hiking"]  # Key "hobbies" maps to a list of hobbies
    },
    "address": {                              # Key "address" maps to another dictionary
        "city": "New York",                   # Key "city" in the nested dictionary
        "zip": "10001"                        # Key "zip" in the nested dictionary
    }
}

# Print the entire advanced dictionary
print("\nAdvanced Dictionary - Nested dictionary:", adv_dict)
# Accessing the list of hobbies within the nested dictionary
print("Advanced Dictionary - Hobbies:", adv_dict["details"]["hobbies"])  # Accessing the list under "details"
# Accessing the city from the nested address dictionary
print("Advanced Dictionary - City:", adv_dict["address"]["city"])  # Accessing the value under "address"
