import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry! Too low! Try again!")
        elif guess > random_number:
            print("Sorry! Too high! Try again!")

    print(f'Jackpot! You have guessed the number {random_number} correctly!')


user_guess(10)
