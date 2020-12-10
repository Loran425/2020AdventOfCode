#!/usr/bin/env python
# Solution to the AOC2020 Challenge 1/2
# https://adventofcode.com/2020/day/1

# GOAL 1: Return the product of the two integers that sum to 2020
# GOAL 2: Return the product of the three integers that sum to 2020

def find_sum(recipts, sum):
    for x in recipts:
        for y in recipts:
            if x+y == sum:
                return x, y


def find_advance_sum(recipts, sum):
    for x in recipts:
        for y in recipts:
            for z in recipts:
                if x+y+z == sum:
                    return x, y, z


if __name__ == '__main__':
    recipts = []

    with open("input.txt", "r") as f:
        for line in f:
            recipts.append(int(line))

    x1, y1 = find_sum(recipts, 2020)
    x2, y2, z2 = find_advance_sum(recipts, 2020)

    print(f"2 Item Sum: {x1} {y1}")
    print(f"Product: {x1 * y1}")
    print(f"3 Item Sum: {x2} {y2} {z2}")
    print(f"Product: {x2 * y2 * z2}")
