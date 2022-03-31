#!/usr/bin/env python3

import sys


def rot_char(c, rotation=13):
    if c.isupper():
        from string import ascii_uppercase as letters
    elif c.islower():
        from string import ascii_lowercase as letters
    else:
        raise ValueError("Cannot encode a non-letter.")

    rotted_letters = letters[rotation:] + letters[:rotation]

    return rotted_letters[letters.find(c)]


def rot_word(word, rotation=13):
    return ''.join([rot_char(c)
                    if c.isalpha() else c
                    for c in word])


if __name__ == '__main__':
    try:
        print(f'{sys.argv[1]} -> {rot_word(sys.argv[1])}')
        print(f'{sys.argv[1]} -> {rot_word(sys.argv[1])} -> {rot_word(rot_word(sys.argv[1]))}')
    except IndexError:
        print('Nothing to ROT. Nothing to do.')
