# Exercise 3: Biography

# for the user to enter details
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# To ensure that the age is an integer 
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Please enter a valid integer for age.")

# storing the information in an dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print the values on separate lines using a single print() statement
print(f"\nName: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")
