#!/usr/bin/env python3


from random import randint


def generate_secret_number():
    """
        Generate number. Cannot be divisible by 5.
    """
    while True:
        possible_secret = randint(0, 100)

        if possible_secret % 5 != 0:
            return possible_secret


def get_guess(previous_guesses):
    """
        Read player guess, validate, compare with previous guesses, and return.
    """
    while True:
        try:
            new_guess = int(input('Enter your guess: '))
            if 0 <= new_guess <= 100 and new_guess not in previous_guesses:
                return new_guess
            elif new_guess in previous_guesses:
                print('You guessed that before. Try again.')
            else:
                print('Error. Guess must be between 0 and 100.')
        except ValueError:
            print('Error. Please enter an integer.')


if __name__ == '__main__':

    secret = generate_secret_number()
    guesses = 0
    list_of_guesses = []

    while True:

        this_guess = get_guess(list_of_guesses)

        list_of_guesses.append(this_guess)
        guesses += 1

        if secret != this_guess:
            print(f'The secret number is {"higher" if secret > this_guess else "lower"} than your guess.')
        else:
            print('You got it right!')
            break

        if guesses == 10:
            print(f'You ran out of guesses. The secret number was {secret}.')
            break
