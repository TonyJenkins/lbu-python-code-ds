#!/usr/bin/env python3


from random import randint, shuffle, uniform


DRIVERS = [
    ['HAM', 'Mercedes'],
    ['BOT', 'Mercedes'],
    ['VER', 'Red Bull'],
    ['PER', 'Red Bull'],
    ['RUS', 'Williams'],
    ['LAT', 'Williams'],
    ['SAI', 'Ferrari'],
    ['LEC', 'Ferrari'],
    ['NOR', 'McLaren'],
    ['RIC', 'McLaren'],
    ['GAS', 'Alpha Tauri'],
    ['TSU', 'Alpha Tauri'],
    ['ALO', 'Alpine'],
    ['OCO', 'Alpine'],
    ['VET', 'Aston Martin'],
    ['STR', 'Aston Martin'],
    ['RAI', 'Alfa Romeo'],
    ['GIO', 'Alfa Romeo'],
    ['SCH', 'Haas'],
    ['MAZ', 'Haas'],
]

MAX_LAPS = 60
MIN_LAPS = 30

MAX_LAP_TIME = 120
MIN_LAP_TIME = 110

TOP_TEAM = ['Mercedes', 'Red Bull']
MIDDLE_TEAM = ['McLaren', 'Ferrari', 'Alpine', 'Alpha Tauri']

OUTPUT_FILE = 'lap_times.txt'

if __name__ == '__main__':

    lap_times = []

    for driver in DRIVERS:
        for lap in range(randint(MIN_LAPS, MAX_LAPS)):
            if driver[0] == 'HAM':
                min_lap_time = MIN_LAP_TIME - 3
                max_lap_time = MAX_LAP_TIME -2
            elif driver[1] in TOP_TEAM:
                min_lap_time = MIN_LAP_TIME - 1.5
                max_lap_time = MAX_LAP_TIME - 2
            elif driver[1] in MIDDLE_TEAM:
                min_lap_time = MIN_LAP_TIME - 1
                max_lap_time = MAX_LAP_TIME + 1
            else:
                min_lap_time = MIN_LAP_TIME
                max_lap_time = MAX_LAP_TIME + 2
            lap_times.append(f'{driver[0]},{driver[1]},{uniform(min_lap_time, max_lap_time):.3f}')

    shuffle(lap_times)

    with open(OUTPUT_FILE, 'w') as out:
        for lap_time in lap_times:
            out.write(lap_time + '\n')
