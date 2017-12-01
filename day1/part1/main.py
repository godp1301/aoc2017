#!/usr/bin/env python

from day1 import puzzle_input


def run(value):
    sum = 0
    try:
        for i, c in enumerate(value):
            if value[i] == value[i+1]:
                sum += int(c)
    except IndexError:
        if value[0] == value[len(value)-1]:
            sum += int(value[0])
    print(sum)
    return sum


if __name__ == '__main__':
    run(puzzle_input)
