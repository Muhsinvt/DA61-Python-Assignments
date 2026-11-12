# Python Assignment 3: While Loop, For Loop and Function

# =========================================================
# WHILE LOOP & CONTROL STATEMENTS - Number Guessing Game
# =========================================================
import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 3   # maximum number of valid guesses allowed

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    # Out of range: inform the user and skip the rest of the loop (attempt not used)
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    attempts -= 1   # a valid guess uses one attempt

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
else:
    # Runs only if the loop ends without break (attempts used up)
    print("Better luck next time! The number was", secret_number)

# =========================================================
# FOR LOOP - Multiplication Table Generator
# =========================================================
num = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

# =========================================================
# FUNCTION - BMI Calculator
# =========================================================
def calculate_bmi(weight, height):
    """Return BMI = weight (kg) / height (m) squared."""
    return weight / (height ** 2)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")