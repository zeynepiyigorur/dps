#!/usr/bin/env python3

# Prints a snake table from any array of any type and creates a snake table of any amount of rows. Default is 2 rows.
def print_snake_table(arr, rows=2):
    end_rows = min(len(arr), rows)
    lines = []
    for _ in range(0, end_rows):
        lines.append([])

    divider = rows * 2

    for index, element in enumerate(arr):
        remainder = index % divider
        if remainder < rows:
            lines[remainder].append(element)
        else:
            lines[divider - remainder - 1].append(element)

    for line in lines:
        for element in line:
            print(element, end="")
        print("")


print_snake_table(input("Enter input: "), int(input("Enter number of rows: ")))
