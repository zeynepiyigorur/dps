#!/usr/bin/env python3

# Implementation generalized for all input types
# Prints a snake table from any array (collection) of any type
def print_snake_table(arr):
    lines = [[], []]

    for index, element in enumerate(arr):
        remainder = index % 4
        if remainder < 2:
            lines[remainder].append(element)
        else:
            lines[4 - remainder - 1].append(element)

    for line in lines:
        for element in line:
            print(element, end="")
        print("")


# Example code demonstrating universal object handling
# Example Object Wrapper to demonstrate that this snake table implementation works on any array of any type
class ExampleObjectWrapper:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return str(self.content)


print_snake_table([ExampleObjectWrapper(content='1'),
                   ExampleObjectWrapper(content=2),
                   ExampleObjectWrapper(content=ExampleObjectWrapper(content='3')),
                   ExampleObjectWrapper(content="4"),
                   5,
                   ExampleObjectWrapper(content="Six")])
