# Step 1: Import the random module
import random

# Step 2: Define a function with a parameter
def compare_numbers(user_number):
    if not isinstance(user_number, int) or not (1 <= user_number <= 100):
        raise ValueError("The parameter must be an integer between 1 and 100.")

    # Step 3: Generate a random number
    random_number = random.randint(1, 100)

    # Step 4: Compare the numbers
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Step 5: Call the function
compare_numbers(50)