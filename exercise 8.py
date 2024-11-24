# Exercise 8: Simple Search

# Create a list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a name to search for
search_name = input("Enter name to search: ")

# Check if the entered name is in the list
if search_name in names:
    print("Name found in list")
else:
    print("Name not found in list")

