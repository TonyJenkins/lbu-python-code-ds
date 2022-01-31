#!/usr/bin/env python3

if __name__ == '__main__':

    eggs = int(input('How many eggs do we have? '))

    boxes = eggs // 6
    left_over = eggs % 6

    print(f'We need {boxes} boxes. There will be {left_over} extra eggs.')
