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


def rotter(word, rotation=13):
    return ''.join([rot_char(c)
                    if c.isalpha() else c
                    for c in word])


def rot_file(filename, extension='_rotted'):
    with open(filename) as infile, open(filename + extension, 'w') as outfile:
        outfile.write(rotter(infile.read()))


if __name__ == '__main__':
    try:
        rot_file(sys.argv[1])
    except IndexError:
        print('No filename given. Nothing to do.')
    except FileNotFoundError:
        print(f'Could not open "{sys.argv[1]}". Sorry about that.')
    except PermissionError:
        print('Missing permission to write output file. How sad.')
    except OSError:
        print('Something terrible happened. Maybe the disk is full.')
