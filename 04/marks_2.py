#!/usr/bin/env python3


def avg(numbers):
    return sum(numbers) / len(numbers)


if __name__ == '__main__':

    marks = []

    finished = False

    while not finished:
        while True:
            mark = input('Enter Mark: ')
            if not mark:
                finished = True
                break
            try:
                if 0 <= int(mark) <= 100:
                    marks.append(int(mark))
                    break
                else:
                    print('Out of range! Try again.')
            except ValueError:
                print('Not a number! Try again.')
    if marks:
        highest_mark = max(marks)
        lowest_mark = min(marks)
        average_mark = avg(marks)

        print()
        print(f'Highest Mark: {highest_mark:6}')
        print(f'Lowest Mark:  {lowest_mark:6}')
        print(f'Average Mark: {average_mark:6.2f}')
    else:
        print('No marks entered.')
