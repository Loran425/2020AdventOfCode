#!/usr/bin/env python
# Solution to the AOC2020 Challenge 3/4
# https://adventofcode.com/2020/day/2

# GOAL 1: Return the number of "passwords" that have char in the range give
# GOAL 2: Return the number of "passwords" that have char at only 1 location.

def sled_password_check(password: str, char, min, max):
    return min <= password.count(char) <= max

def toboggan_password_check(password, char, pos1, pos2):
    return password[pos1] == char and password[pos2] != char or password[pos2] == char and password[pos1] != char


valid_sled_passwords = 0
valid_toboggan_passwords = 0

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        for line in f:
            pre, password = line.split(":")
            mM, char = pre.split()
            m, M = [int(x) for x in mM.split("-")]
            if sled_password_check(password, char, m, M):
                valid_sled_passwords += 1
            if toboggan_password_check(password, char, m, M):
                valid_toboggan_passwords += 1

    print(f"Found {valid_sled_passwords} Valid Sled Passwords")
    print(f"Found {valid_toboggan_passwords} Valid Toboggan Passwords")
