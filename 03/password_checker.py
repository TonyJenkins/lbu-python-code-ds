#!/usr/bin/env python3


if __name__ == '__main__':

    password = input('Enter password to check: ')

    has_upper = has_lower = has_digit = has_special = False

    for letter in password:
        if letter.isupper():
            has_upper = True
        elif letter.islower():
            has_lower = True
        elif letter.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print('Password OK')
    else:
        print('Password fails complexity check.')
