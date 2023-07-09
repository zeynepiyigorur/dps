#!/usr/bin/env python3

# Implementation optimized for strings
# Prints a snake table from an array of chars (an array of symbols)
def print_snake_table(arr):
    lines = ['', '']

    for index, element in enumerate(arr):
        remainder = index % 4
        if remainder < 2:
            lines[remainder] += element
        else:
            lines[4 - remainder - 1] += element

    for line in lines:
        print(line)


print_snake_table(input("Enter symbols: "))
