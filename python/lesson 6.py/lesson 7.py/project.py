import random

# Game data stored using a dictionary
game_data = {
    "target_number": random.randint(1, 100),
    "max_attempts": 10,
    "attempts": 0,
    "guesses": []  # This will be a list of guesses
}

print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {game_data['max_attempts']} attempts to guess it!")

while game_data["attempts"] < game_data["max_attempts"]:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    game_data["guesses"].append(guess)
    game_data["attempts"] += 1

    if guess == game_data["target_number"]:
        print(f" Congratulations! You guessed it in {game_data['attempts']} attempts.")
        break
    elif guess < game_data["target_number"]:
        print("📉 Too low! Try a higher number.")
    else:
        print("📈 Too high! Try a lower number.")

# If the user doesn't guess the number
if game_data["attempts"] == game_data["max_attempts"] and guess != game_data["target_number"]:
    print(f" Game Over! The number was {game_data['target_number']}.")

# Display all guesses
print("📋 Your guesses were:", game_data["guesses"])
