import random
import time

BULLETS = "-" * 50

def print_intro() -> None:
    """Prints the game introduction and rules."""
    print("Hi there!")
    print(BULLETS)
    print(
        "I've generated a random 4 digit number for you.\n"
        "Let's play a bulls and cows game."
    )
    print(BULLETS)


def count_bulls_and_cows(secret: str, guess: str) -> tuple[int, int]:
    """
    Counts bulls and cows between secret number and guessed number.

    Bull = correct digit in correct position
    Cow  = correct digit in wrong position
    """
    bulls = 0
    cows = 0

    for secret_digit, guess_digit in zip(secret, guess):
        if secret_digit == guess_digit:
            bulls += 1
        elif guess_digit in secret:
            cows += 1

    return bulls, cows


def is_valid_guess(guess: str) -> bool:
    """Validates user input according to game rules."""
    if len(guess) != 4:
        return False
    if not guess.isdigit():
        return False
    if guess[0] == "0":
        return False
    if len(set(guess)) != 4:
        return False
    return True


def ask_yes_no(prompt: str) -> bool:
    """
    Asks the user a yes/no question and validates the input.

    Returns:
        True if user answers yes
        False if user answers no 
    """
    while True:    
        answer = input(prompt).lower().strip()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        
        print(BULLETS)
        print("Invalid input. Please enter y/n.")
        print(BULLETS)


def generate_num() -> str:
    """Generates a random 4-digit number with unique digits and no leading zero."""
    first_digit = random.choice("123456789")
    remaining_digits = "0123456789".replace(first_digit, "")
    other_digits = random.sample(remaining_digits, 3)
    return first_digit + "".join(other_digits)


def play_game(stats: list[int]) -> None:
    """Runs a single game session."""
    print_intro()
    secret = generate_num()
    attempts = 0
    start_time = time.time()
        
    while True:
        guess = input("Enter a number: ").strip()

        if not is_valid_guess(guess):
            print("Invalid input. Please enter 4 unique digits.")
            print(BULLETS)
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)

        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"

        print(f"{bulls} {bull_word}, {cows} {cow_word}")
        print(BULLETS)
        
        if bulls == 4:
            duration = round(time.time() - start_time, 2)
            print("Correct, you've guessed the right number!")
            print(f"Attempts: {attempts}")
            print(f"Time: {duration} seconds")
            print(BULLETS)
            stats.append(attempts)
            break


def main() -> None:
    """Main program loop."""
    game_stats: list[int] = []

    while True:
        play_game(game_stats)
        if not ask_yes_no("Do you want to play again? (y/n): "):
            break

    if game_stats:
        print(BULLETS)
        print("Game statistics:")
        print(f"Games played: {len(game_stats)}")
        print(f"Attempts per game: {game_stats}")
        print(f"Best game: {min(game_stats)} attempts")
        print(f"Average attempts: {round(sum(game_stats) / len(game_stats), 2)}")


if __name__ == "__main__":
    main()