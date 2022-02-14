#!/usr/bin/env python3


if __name__ == '__main__':

    marks = []

    finished = False

    while not finished:
        while True:
            mark = input('Enter Mark: ')
            if not mark:
                finished = True
                break
            elif 0 <= int(mark) <= 100:
                marks.append(int(mark))
                break
            else:
                print('Out of range! Try again.')

    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = sum(marks) / len(marks)

    print()
    print(f'Highest Mark: {highest_mark:6}')
    print(f'Lowest Mark:  {lowest_mark:6}')
    print(f'Average Mark: {average_mark:6.2f}')
