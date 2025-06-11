import random

def number_guess_game():
    print("🎮 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess (1-100): "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guess_game()
