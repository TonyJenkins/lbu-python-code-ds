#!/usr/bin/env python3

NUMBER_OF_MARKS = 5

if __name__ == '__main__':

    marks = []

    for count in range(NUMBER_OF_MARKS):
        while True:
            mark = int(input('Enter Mark: '))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print('Out of range! Try again.')

    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = sum(marks) / NUMBER_OF_MARKS

    print()
    print(f'Highest Mark: {highest_mark:6}')
    print(f'Lowest Mark:  {lowest_mark:6}')
    print(f'Average Mark: {average_mark:6.2f}')
