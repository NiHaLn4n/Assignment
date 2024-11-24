# Creating a dictionary with nations as keys and their capitals as values
nation = {"Albania": "Tirana",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Ireland": "Dublin",
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Russia": "Moscow",
    "United Kingdom": "London",
    "Spain": "Madrid"}

# Initialize the score to 0
score = 0
# Get the total number of nations in the dictionary
total = len(nation)

# Iterate through each nation and its capital in the dictionary
for nation, capital in nation.items():
    # Prompt the user to input the capital of the current nation
    response = input(f"What is the capital of {nation}? ").strip()
    # Check if the user's response matches the capital (case insensitive)
    if response.capitalize() == capital.capitalize():
        # If the user's response matches the capital, print "Correct!" and increment the score
        print("Correct!")
        score += 1
        print()  # Print an empty line for spacing
    else:
        # If the user's response does not match the capital, print the correct capital
        print(f"Wrong! The capital of {nation} is {capital}.")
        print()  # Print an empty line for spacing

# Print the final score out of the total number of nations
print(f"\nScore: {score}/{total}")
