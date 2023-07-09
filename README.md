## Setup
* Open a terminal
* Make sure you have python3 installed
* Go to the directory where you cloned this repository to
* Execute any version by typing e.g. <code>./snake_table_variable_rows.py</code> in the terminal
* If it doesn't work: type <code>chmod +x *.py</code> and then run again

## Different implementations
The file [snake_table_first_idea](./snake_table_first_idea.py) is my first idea when I looked at this task. I then
expanded on this idea but I still left it in so that my thought process is included.

The file [snake_table_string](./snake_table_string.py) contains an optimized implementation specifically tailored to
strings. In python, strings are simply collections of characters, so this implementation matches the given task and 
example. This implementation runs with an efficiency of O(n) where n is the number of symbols.

The file [snake_table_all_input_types](./snake_table_all_input_types.py) generalizes this implementation to
support collections of any type. A demonstration is appended. This also runs in O(n).

Finally, the file [snake_table_variable_rows](./snake_table_variable_rows.py) generalizes the implementation further
by supporting all data types within a collection and furthermore allowing for a dynamic amount of rows; i.e. if the 
"snake" is supposed have a vertical space of x rows, this can be supported without restriction. The implementations 
before consider only two rows. If the specified number of rows is greater than the amount of elements in the array, it 
will prune the output and simply print one element per line. This also runs in O(n).
After coming up with this implementation, I also improved [snake_table_string](./snake_table_string.py) and 
[snake_table_all_input_types](./snake_table_all_input_types.py) to use the general formula I found.

## Limitations
* Printing to the terminal can be improved by considering the length of individual elements.