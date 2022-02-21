#!/usr/bin/env python3

if __name__ == '__main__':

    try:
        top = int(input('Enter top number: '))
        bottom = int(input('Enter bottom number: '))
        print(f'{top}/{bottom} = {top / bottom}')

    except ValueError:
        print("Enter a number!")
    except ZeroDivisionError:
        print('Cannot divide by zero!')
