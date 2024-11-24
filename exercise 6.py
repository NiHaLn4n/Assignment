#Exercise 6: Brute Force Attack

# Define the correct password
password = "12345"

# Initialize the number of attempts
attempts = 0
max_attempts = 5  # Maximum number of allowed attempts

# Start a loop that runs until the maximum number of attempts is reached
while attempts < max_attempts:
    # Prompt the user to enter the password
    user_input = input("Enter your password: ")

    # Check if the user input matches the correct password
    if user_input == password:
        print("Access granted")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1  # Increment the number of attempts
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Access denied. Try again! You have {remaining_attempts} attempts left.")
        else:
            print("Access denied.maximum number of attempts reached.")
            print("Authorities have been alerted.")  # Inform the user that authorities have been alerted
            break  # Exit the loop
