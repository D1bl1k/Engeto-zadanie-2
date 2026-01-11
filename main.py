import random
import time
bullets = '-' * 50
#Funkcia na vypisanie uvodu 
def print_intro() -> None:
    print("Hi there!")
    print(bullets)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(bullets)
#zde sa pocitaju bulls a cows 
def count_bulls_and_cows(hide_num: str, guessed_number: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for num in range(len(hide_num)):
        if hide_num[num] == guessed_number[num]:
            bulls += 1
        elif guessed_number[num] in hide_num:
            cows += 1
    return bulls, cows
#ci je dane cislo spravne zapisane 
def is_valid_gues(guessed_number: str) -> bool:
    if len(guessed_number) != 4:
        return False
    if not guessed_number.isdigit():
        return False
    if guessed_number[0] == "0":
        return False
    if len(set(guessed_number)) != 4:
        return False
    return True
#generuje sa nahodne cislo
def generate_num() -> str:
    first_num = random.choice("123456789")
    remaining_num = "0123456789".replace(first_num, "")
    other_num = random.sample(remaining_num, 3)
    secret = first_num + "".join(other_num)
    return secret
#jedna hra
def play_game(stats: list[int]) -> None:
    print_intro()
    hide_num = generate_num()
    attempts = 0
    start_time = time.time()
    while True :
        guessed_number = input("Enter a number:").strip()
        if not is_valid_gues(guessed_number):
            print("Invalid input. Please enter 4 unique number.")
            print(bullets)
            continue
        attempts += 1
        bulls, cows = count_bulls_and_cows(hide_num, guessed_number)
        print(f"{bulls} bulls, {cows} cows")
        print(bullets)
        if bulls == 4 :
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print("Correct, you've guessed the right number")
            print(f"Attempts: {attempts}")
            print(f"Time: {duration} seconds")
            print(bullets)
            stats.append(attempts)
            break   
#spustenie hry 
def main() -> None:
    game_stats = []
    while True:
        play_game(game_stats)
        again = input("Do you want to play again? (y/n): ").lower().strip()
        if again != "y":
            break
    if game_stats:
        print(bullets)
        print("\nGame statistics:")
        print(f"Games played: {len(game_stats)}")
        print(f"Attempts per game: {game_stats}")
        print(f"Best game: {min(game_stats)} attempts")
        print(f"Average attempts: {round(sum(game_stats) / len(game_stats), 2)}")

if __name__ == "__main__":
    main()











