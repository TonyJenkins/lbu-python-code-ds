#!/usr/bin/env python3


from statistics import mean, StatisticsError


def avg(marks):
    """
        'Average' mark calculated ignoring the lowest mark.

        If only one mark present, it is returned as 'Average'.
    """

    try:
        marks.sort(reverse=True)
        return mean(marks[:-1])
    except StatisticsError:
        return mean(marks())


def read_marks():
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

    return marks


def letter_grade(marks):

    try:
        mark = avg(marks)

        if mark > 70:
            return 'A'
        elif mark > 60:
            return 'B'
        elif mark > 50:
            return 'C'
        elif mark > 40:
            return 'D'
        else:
            return 'F'

    except ValueError:
        return 'X'


def display_results(marks):
    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = mean(marks)

    print()
    print(f'Highest Mark: {highest_mark:6}')
    print(f'Lowest Mark:  {lowest_mark:6}')
    print(f'Average Mark: {average_mark:6.2f}')

    print(f'Grade:        {letter_grade(marks):>6}')


if __name__ == '__main__':

    grades = read_marks()

    if grades:
        display_results(grades)
    else:
        print()
        print('No marks entered.')
