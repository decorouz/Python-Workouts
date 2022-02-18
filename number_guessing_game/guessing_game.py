import random


def guessing_game():
    secret_number = random.randint(10, 100)
    try_count = 3

    while try_count:
        try_count -= 1
        user_guess = int(input("Please guess a number: "))

        if user_guess == secret_number:
            print(f"Right! The answer is {user_guess}")
            break
        if user_guess < secret_number:
            print(f"Your guess of {user_guess} is too low ")
        else:
            print(f"Your guess of {user_guess} is too high!")
    print(
        f"You didn't guess the current number {secret_number} after the allowed attempts!")


guessing_game()
