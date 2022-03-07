#!/usr/bin/env python3


from statistics import mean


def c2f(celsius):
    return (celsius * 9 / 5) + 32


def f2c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def print_results(all_readings):
    highest_temp = max(all_readings)
    lowest_temp = min(all_readings)
    average_temp = mean(all_readings)

    print()
    print(f'Highest Temperature: {highest_temp:6.2f}C {c2f(highest_temp):6.2f}F')
    print(f'Lowest Temperature:  {lowest_temp:6.2f}C {c2f(lowest_temp):6.2f}F')
    print(f'Average Temperature: {average_temp:6.2f}C {c2f(average_temp):6.2f}F')


if __name__ == '__main__':

    readings_in_celsius = []

    while True:

        next_reading = input('Enter a reading: ')

        if not next_reading:
            break

        try:
            if next_reading.endswith(('C', 'c')):
                readings_in_celsius.append(int(next_reading[:-1]))
            elif next_reading.endswith(('F', 'f')):
                readings_in_celsius.append(f2c(int(next_reading[:-1])))
            else:
                print('Error: Reading must end with C or F. Ignoring.')
        except ValueError:
            print('Error. Reading in incorrect format. Ignoring.')

    if readings_in_celsius:
        print_results(readings_in_celsius)
    else:
        print('No data entered. Nothing to do.')
