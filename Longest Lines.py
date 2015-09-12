__author__ = 'leigh'


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

    # sort the list "lines" based on "lines_length"
    for item1 in range(len(lines)):
        for first in range(len(lines_length)):

            # EXAMPLE -> item1 = "cookies are great", item2 = 17
            for second in range(first + 1, len(lines_length)):
                if lines_length[second] < lines_length[first]:
                    # exchanging the numbers
                    lines_length[second], lines_length[first] = \
                        lines_length[first], lines_length[second]

                    # hopefully exchanging the strings
                    lines[second], lines[first] = lines[first], lines[second]

    return list(reversed(lines[-int(number):]))

print(longest_line("C:\\Users\\Leigh\\Desktop\\python_example.txt")[0])
print(longest_line("C:\\Users\\Leigh\\Desktop\\python_example.txt")[1])

