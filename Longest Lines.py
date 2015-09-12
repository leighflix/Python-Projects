__author__ = 'leigh'

""" EXAMPLE FILE
------------------- python_example.txt -----------------------------
3
That leigh guy is pretty awesome
I know right, I totally agree
Could it be that he's greater than we imagine?
Is 42 really the answer to the universe?
no no, I think leigh is the answer... *whispers*, to everything.
--------------------------------------------------------------------

## look at line 49 for the reason the result is like this:
========================== Results =============================
no no, I think leigh is the answer... *whispers*, to everything.
Could it be that he's greater than we imagine?
================================================================
"""

def longest_line(path):
    file = open(path, 'r')

    # lines -> str, lines_length -> int
    lines, lines_length = [], []

    # get the first line (a integer)
    number = file.readline()

    # give the lines to the lists (feed them >:D)
    for line in file:
        lines.append(line)
        lines_length.append(len(line))
        
    # EXAMPLE -> item1 = "cookies are great", item2 = 17
    
    # sort the list "lines" based on "lines_length" (using a bubble sort concept for lists)
    for non_usuable_variable in range(len(lines)):
        for first in range(len(lines_length)):
            for second in range(first + 1, len(lines_length)):
                if lines_length[second] < lines_length[first]:
                    # exchanging the numbers
                    lines_length[second], lines_length[first] = \
                        lines_length[first], lines_length[second]

                    # hopefully exchanging the strings
                    lines[second], lines[first] = lines[first], lines[second]

    return list(reversed(lines[-int(number):]))

# I only want 2 lines, not 3 as stated in the 'python_example.txt' file. so I used this>
print(longest_line("C:\\Users\\Leigh\\Desktop\\python_example.txt")[0])
print(longest_line("C:\\Users\\Leigh\\Desktop\\python_example.txt")[1])

