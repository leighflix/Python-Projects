__author__ = 'leigh'

# function from "mhawke" from stack over flow or from here:
# (http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list)
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def validate(phone_number):
    phone_number = list(phone_number)

    # if dashed version of phone number (123-456-7890) or
    # if dotted version of phone number (123.456.7890)
    if len(phone_number) == 12:
        if '-' in phone_number:
            phone_number = remove_values_from_list(phone_number, '-')
            # is all of the numbers are between 0-9 (1, 2.. 9) and len(#) is == to 10
            return all(int(i) <= 9 for i in phone_number) and len(phone_number) == 10

        elif '.' in phone_number:
            phone_number = remove_values_from_list(phone_number, '.')
            # The idea of returning "True" if the length of 'phone_number'
            # is 10 is only true with all characters are within 0-9
            # that being that the (.) or (-) is removed.
            return all(int(i) <= 9 for i in phone_number) and len(phone_number) == 10

    if len(phone_number) == 13 or 14:
        # removing multiple items
        for i in ['-', '(', ')', ' ']:
            phone_number = remove_values_from_list(phone_number, i)
        try:
            return all(int(i) <= 9 for i in phone_number) and len(phone_number) == 10
        except ValueError:
            print("Invalid Character!!!")

    # if numbered version of phone number (1234567890)
    if len(phone_number) == 10:
        try:
            return all(int(i) <= 9 for i in phone_number) and len(phone_number) == 10
        except ValueError:
            print("Invalid Character!!!")

typed = input("input a telephone #: ")

while typed != "quit":
    if validate(typed):
        print("The Telephone Number {} is valid.".format(typed))
    elif not validate(typed):
        print("The Telephone Number {} is not valid.".format(typed))
    typed = input("\ninput a telephone #: ")

