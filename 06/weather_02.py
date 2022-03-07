#!/usr/bin/env python3

def avg(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ValueError:
        raise ValueError ('Empty sequence passed to average function')


def c2f (celsius):
    return (celsius * 9 / 5) + 32


def f2c (fahrenheit):
    return (fahrenheit - 32) / (9 / 5)


def chomp (s):
    return s[:-1]


def read_values():
    print('Enter the daily readings. Hit "Enter" to end.')

    readings_in_celsius = []

    while True:
        next_reading = input ('--> ')
        if not next_reading:
            break

        try:
            if next_reading.upper().endswith('C'):
                readings_in_celsius.append(float(chomp(next_reading)))
            elif next_reading.upper().endswith('F'):
                readings_in_celsius.append(f2c(float(chomp(next_reading))))
            else:
                print('Error in input. Missing temperature scale?')
        except ValueError:
            print('Error in input. Incorrect format?')

    return readings_in_celsius


def temp_string(temp_in_celsius):
    return f'{temp_in_celsius:6.2f}C {c2f(temp_in_celsius):6.2f}F'


def print_statistics(readings_in_celsius):
    print()
    print(f'Average Temperature: {temp_string(avg(readings_in_celsius))}')
    print(f'Maximum Temperature: {temp_string(max(readings_in_celsius))}')
    print(f'Minimum Temperature: {temp_string(min(readings_in_celsius))}')


if __name__ == '__main__':

    readings = read_values()

    if readings:
        print_statistics(readings)
    else:
        print('No data entered. Nothing to do.')
