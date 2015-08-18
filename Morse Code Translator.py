__author__ = 'leigh'

import re

''' To split the strings, I'm using Regular Expressions.

The reason for this is purely so I can use multiple delimeters.

Example:

    s = "..-..- -.. -.. --- / .--..- - -..."
    re.split(' |/ ', s)

Mostly because I feel more comfortable using this as well.

And for the multiple delimeters, I might update or change how
lists are formed using "spaces" or "slashes", so I might as well
just use it anyways. (not worrying about efficiency anyways)
'''


Morse_Alphabet = {
    "a" : ".-",     "b" : "-...",     "c" : "-.-.",
    "d" : "-..",    "e" : ".",        "f" : "..-.",
    "g" : "--.",    "h" : "....",     "i" : "..",
    "j" : ".---",   "k" : "-.-",      "l" : ".-..",
    "m" : "--",     "n" : "-.",       "o" : "---",
    "p" : ".--.",   "q" : "--.-",     "r" : ".-.",
    "s" : "...",    "t" : "-",        "u" : "..-",
    "v" : "...-",   "w" : ".--",      "x" : "-..-",
    "y" : "-..--",  "z" : "--.."
}

def read(morse_code):
    ''' Reads the string argument "morse_code", and translates to based on strings

    Returns a string
    '''

    # splits the string into a list, which is duplicated.
    secondary_list = morse_list = re.split(' ', morse_code)

    for item in range(len(morse_list)):
        for item2, item3 in Morse_Alphabet.items():

            # using another list simply for keeping track
            # of the items. And in-case of the first list
            # being buggy/manipulated wrong.
            if morse_list[item] == item3:
                secondary_list[item] = item2
            elif morse_list[item] == "/":
                secondary_list[item] = " "

    # converts the list into a string and returns it.
    return ''.join(secondary_list)

def translate(text):
    ''' Reads the string argument "text", and translated to to morse code based on lists.

    Returns a string in morse code format (text formatted into morse code)
    '''

    secondary_list = text_list = list(text)

    for item in range(len(text_list)):
        for item2, item3 in Morse_Alphabet.items():

            # same situation as in read()
            if text_list[item] == item2:
                secondary_list[item] = item3 + " "
            elif text_list[item] == " ":
                secondary_list[item] = "/ "

    return ''.join(secondary_list)

def main():
    print("\n-=[Morse Code translator]=-\n\tBy Leigh\n")
    print("For help, input 'help()'")

    ask = input("#] ")
    while ask != "quit()":

        if ask == "read()":
            morse = input("| ")
            print("text: " + read(morse) + "\n")

        elif ask == "translate()":
            text = input("| ")
            print("morse: " + translate(text) + "\n")

        elif ask == "help()":
            print("The slash(/) seperates the morse 'words', and the spaces( ) seperate morse letters\n")
            print("To translate from morse to text, type 'read()'")
            print("To translate from text to morse, type 'translate()'")
            print("To quit, type 'quit()'\n")

        else: print("No known keyword: " + ask)

        ask = input("#] ")

if __name__ == "__main__":
    main()
