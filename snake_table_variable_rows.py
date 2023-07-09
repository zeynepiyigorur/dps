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


number_of_rows_string = input("Enter number of rows: ")
if not number_of_rows_string.isdigit():
    print("Please enter a valid number of rows")
else:
    if int(number_of_rows_string) < 1:
        print("Please enter a strictly positive number of rows")
    else:
        user_input = input("Enter input: ")
        print_snake_table(user_input, int(number_of_rows_string))
