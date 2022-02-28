#!/usr/bin/env python3


from areas import circle_area


if __name__ == '__main__':
    radius = int(input('Enter the Radius: '))
    
    print(f'Area is {circle_area(radius)}')
