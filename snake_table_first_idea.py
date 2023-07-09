#!/usr/bin/env python3

# This is my first attempt at solving the problem, this is the simplest solution
# This is here to illustrate my thought process

def print_snake_table(arr):
    line1 = ''
    line2 = ''
    for index, char in enumerate(arr):
        if index % 4 in [0, 3]:
            line1 += char
        else:
            line2 += char

    print(line1 + '\n' + line2)


print_snake_table(input("Enter symbols: "))