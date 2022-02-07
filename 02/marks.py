#!/usr/bin/env python3

if __name__ == '__main__':

    mark_1 = int(input('Enter Mark #1: '))
    mark_2 = int(input('Enter Mark #2: '))
    mark_3 = int(input('Enter Mark #3: '))
    mark_4 = int(input('Enter Mark #4: '))
    mark_5 = int(input('Enter Mark #5: '))

    highest_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    lowest_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    average_mark = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5

    print()
    print(f'Highest Mark: {highest_mark:6}')
    print(f'Lowest Mark:  {lowest_mark:6}')
    print(f'Average Mark: {average_mark:6.2f}')
