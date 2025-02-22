import datetime


def get_user_info():
    # This line defines a function named `get_user_info` that takes no arguments.

    # Get User's Name
    while True:
        name = input("Enter your name (max 10 characters): ").title()
        if len(name) > 0:
            break
        else:
            print("Name cannot be empty. Please enter a valid name.")
    # This line prompts the user to enter their name, with a maximum of 10 characters.
    # The `[:10]` slice is used to truncate the input to 10 characters if it is longer.

    # Get User's Sex
    while True:
        sex = input("Enter your sex (M/F): ").upper()
        if sex in ['M', 'F']:
            break
        print("Invalid input. Please enter 'M' or 'F'.")
    # This line prompts the user to enter their sex, which is converted to uppercase using the `upper()` method.

    # Get User's Civil Status
    while True:
        civil_status = input("Enter your civil status (S/M): ").upper()
        if civil_status in ['S', 'M']:
            break
        print("Invalid input. Please enter 'S' or 'M'.")
    # This line prompts the user to enter their civil status, which is converted to uppercase using the `upper()` method.

    # Get User's Birthdate
    while True:
        birthdate_str = input("Enter your birthdate (MM/DD/YYYY): ")
        try:
            birthdate = datetime.datetime.strptime(
                birthdate_str, "%m/%d/%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please enter in MM/DD/YYYY format.")
    # This line prompts the user to enter their birthdate in the format MM/DD/YYYY.
    # This line converts the birthdate string to a `datetime.date` object using the `strptime()` function.

    # Determine User's Title
    title = "Mr." if sex == 'M' else ("Ms." if civil_status == 'S' else "Mrs.")
    # This line determines the user's title based on their sex and civil status.

    # Calculate User's Age

    age = calculate_age(birthdate)
    # This line calls the `calculate_age()` function to calculate the user's age.

    # Determine if User is a Senior
    is_senior = age >= 60
    # This line determines if the user is a senior (i.e., 60 years or older).

    # Return User's Information
    return name, title, is_senior, age, sex, civil_status
    # This line returns the user's name, title, and senior status.

# Function `calculate_age()`


def calculate_age(birthdate):
    # This line defines a function named `calculate_age` that takes one argument: `birthdate`.

    # Get Today's Date
    today = datetime.date.today()
    # This line gets the current date using the `today()` function.

    # Calculate Age
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    # This line calculates the user's age by subtracting their birth year from the current year, and then adjusting for the month and day.

    # Return Age
    return age
    # This line returns the calculated age.

# Example usage:
# name, title, is_senior = get_user_info()
# print(f"Name: {title} {name}")
# print(f"Senior: {is_senior}")
