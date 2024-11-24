# Creating a dictionary with countries as keys and their capitals as values
nation = {
    "Albania": "Tirana",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Ireland": "Dublin",
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Russia": "Moscow",
    "United Kingdom": "London",
    "Spain": "Madrid"
}

# Initialize the score to 0
score = 0
# Get the total number of countries in the dictionary
total = len(nation)

# Iterate through each country and its capital in the dictionary
for country, capital in nation.items():
    # Prompt the user to input the capital of the current country
    response = input(f"What is the capital of {country}? ").strip()
    # Check if the user's response matches the capital (case insensitive)
    if response.capitalize() == capital.capitalize():
        print("Correct!")
        score += 1
        print()
    else:
        print(f"Wrong! The capital of {country} is {capital}.")
        print()

# Print the final score out of the total number of countries
print(f"\nScore: {score}/{total}")
