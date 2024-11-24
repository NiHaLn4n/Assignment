# Exercise 10: Is it even?

# Define a function to check if a number is even or odd
def check_even_or_odd(): 
    # Prompt the user to enter a number and convert it to an integer
    num = int(input("Enter a number: ")) 

    # Check if the number is even
    if num % 2 == 0: 
        print("The number is even")
    else: 
        # If the number is not even, it is odd
        print("The number is odd")

# Call the function to execute it
check_even_or_odd()
