# Define the correct password
password = "12345"

# Start an infinite loop
while True:
    # Prompt the user to enter the password
    user_input = input("Enter your password: ")

    # Check if the user input matches the correct password
    if user_input == password:
        print("Access granted")
        break  # Exit the loop if the password is correct
    else:
        print("Access denied. Try again!")  # Inform the user and continue the loop if the password is incorrect
