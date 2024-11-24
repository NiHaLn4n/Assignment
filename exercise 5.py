# Creating a dictionary with month numbers as keys and days in each month as values
days_in_month = { 
    1: 31, 
    2: 28,  # Default for February; we'll adjust this for leap years
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30, 
    7: 31, 
    8: 31, 
    9: 30, 
    10: 31, 
    11: 30, 
    12: 31
}

# Ask the user to enter a year
user_year = int(input("Enter a year: "))

# Determine if the year is a leap year
if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    is_leap_year = True
    # Adjust February days for a leap year
    days_in_month[2] = 29  
else:
    is_leap_year = False

# Inform the user if it's a leap year or not
if is_leap_year:
    print("This is a Leap Year.")
else:
    print("This is not a Leap Year.")

# Ask the user to enter a month number
month_number = int(input("Enter a month number (1-12): "))

# Check if the entered month number is valid and print the number of days
if month_number in days_in_month:
    # Print the number of days in the specified month
    print(f"{days_in_month[month_number]} days")
else:
    # Print an error message for an invalid month number
    print("Invalid month number.")



         

