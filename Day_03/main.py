#!/usr/bin/env python
# Solution to the AOC2020 Challenge 5/6
# https://adventofcode.com/2020/day/3

# GOAL 1: Return the number of trees encountered on 1:3 slope
# GOAL 2: Return the product of trees encountered on several trajectories

def slope_mapping(map, slope):
    height = len(map)
    width = len(map[0])
    x_pos = 0
    y_pos = 0
    trees = 0
    while True:
        x_pos += slope[0]
        y_pos += slope[1]
        if x_pos >= width:
            x_pos = x_pos % width
        if map[y_pos][x_pos] == "#":
            trees += 1
        if y_pos + slope[1] >= height:
            return trees


if __name__ == '__main__':
    map = []

    with open("input.txt", "r") as f:
        for line in f:
            map.append(line.strip())

    results = {}
    product = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        results[str(slope)] = slope_mapping(map, slope)
        product *= results[(str(slope))]
        print(f"{slope}: Encountered {results[str(slope)]} Trees")

    print(f"product of trees is {product}")


