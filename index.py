import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Iboytech Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
