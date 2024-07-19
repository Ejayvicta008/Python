import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guess = None

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = input("Take a guess (or type 'exit' to quit): ")
        except EOFError:
            print("\nInput stream closed. Exiting game.")
            break
        
        if guess.lower() == 'exit':
            print("Exiting the game. Goodbye!")
            break

        # Ensure input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        number_of_attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()


