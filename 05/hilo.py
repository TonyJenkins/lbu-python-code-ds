#!/usr/bin/env python3


from random import randint


def generate_secret_number():
    while True:
        secret = randint(0, 100)
        if secret not in [25, 50, 75]:
            return secret


def get_guess():
    while True:
        try:
            guess = int(input('Enter your guess: '))
            if 0 <= guess <= 100:
                return guess
            else:
                print('Guesses need to be between 0 and 100!')
        except ValueError:
            print('Enter an integer!')


if __name__ == '__main__':

    secret_number = generate_secret_number()

    guesses = 0

    while True:
        user_guess = get_guess()
        guesses += 1

        if secret_number == user_guess:
            print(f'You guessed my number in {guesses} {"guess" if guesses == 1 else "guesses"}!')
            break
        else:
            print(f'My number is {"higher" if secret_number > user_guess else "lower"} than your guess!')

        if guesses == 10:
            print(f'You ran out of guesses. My number was {secret_number}!')
            break
