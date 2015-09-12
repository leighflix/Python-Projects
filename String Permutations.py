__author__ = 'leigh'

import itertools
from prettytable import PrettyTable

# print all of the possible permutations of the/a string.
# "hi!" ->  "ih!", "i!h", "h!i", "!ih", "!hi", "hi!"

typed = input("Enter String | ")
if len(typed) > 9:
    print("Nope!, nope nope nope, No more than 7 characters.", "\nAre you trying to break this computer?")
else:
    permutations = list(itertools.permutations(typed))
    table = PrettyTable(["Permutation", "index"])
    table.padding_width = 2
    index = 0
    for tuple_list in permutations:
        index += 1
        table.add_row([tuple_list, index])
    print(table)
