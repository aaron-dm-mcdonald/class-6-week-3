# Variables
# Variables store individual pieces of data.
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.5    # Float variable

print("Variable - Name:", name)
print("Variable - Age:", age)
print("Variable - Height:", height)

# Lists
# Lists store ordered collections of items.
fruits = ["apple", "banana", "cherry"]
print("\nList - Fruits:", fruits)
print("List - First fruit:", fruits[0]) # computers count from 0
print("List - Last fruit:", fruits[2]) # last index
print("List - Last fruit:", fruits[-1]) # index-ing backwards works too


# Advanced List
# Lists can contain mixed data types and even other lists.
adv_list = ["text", 123, 45.6, [1, 2, 3], {"key": "value"}]
print("\nAdvanced List - Mixed data types:", adv_list)
print("Advanced List - Nested list:", adv_list[3])
print("Advanced List - Nested list - Single Value:", adv_list[3][1])
print("Advanced List - Dictionary inside list:", adv_list[4])

# Dictionaries
# Dictionaries store unordered collections of key-value pairs.
person = {
    "name": "Bob",
    "age": 25,
    "height": 6.0
}
print("\nDictionary - Person:", person)
print("Dictionary - Name:", person["name"])
print("Dictionary - Age:", person["age"])

# Advanced Dictionary
# Dictionaries can contain nested dictionaries and lists.
adv_dict = {
    "name": "Charlie",
    "details": {
        "age": 28,
        "height": 5.9,
        "hobbies": ["reading", "cycling", "hiking"]
    },
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
print("\nAdvanced Dictionary - Nested dictionary:", adv_dict)
print("Advanced Dictionary - Hobbies:", adv_dict["details"]["hobbies"])
print("Advanced Dictionary - City:", adv_dict["address"]["city"])
