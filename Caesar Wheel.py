__author__ = 'leigh'

# Improve this file.

# "en" stands for "encrypted"
# "de" stands for "decrypted"

def encrypt(en_msg, en_shift):
    encrypted_msg = ""
    # for every letter(character) in the [String](en_msg)
    for letter in en_msg:
        # if the character not capped (etc -> A, B, C)
        if letter.isalpha():
            # v- changes the letter.
            stayIn = ord(letter) + en_shift
            # if the letter exceeds 'z'
            if stayIn > ord('z'):
                stayIn -= 26
            en_final_letter = chr(stayIn)
        if ord(letter) == 32:
            en_final_letter = letter
        # if the final_letter is "space"(32) + shift, then change it back to space(32)
        # if en_final_letter == 32 + en_shift: en_final_letter = 32
        # adding the letters to encrypted_msg like a chain.
        encrypted_msg += en_final_letter
    return encrypted_msg

# return ''.join([])   EXAMPLE

# fundamentally the same as "encrypt(#, #)"
def decrypt(de_msg, de_shift):
    decrypted_msg = ""
    for letter in de_msg:
        if letter.isalpha():
            stayIn = ord(letter) - de_shift
            if stayIn < ord('a'):
                stayIn += 26
            de_final_letter = chr(stayIn)
        if ord(letter) == 32:
            de_final_letter = letter
        # if de_final_letter == 32 - de_shift: de_final_letter = 32
        decrypted_msg += de_final_letter
    return decrypted_msg


def main():
    # plain_text = input("What is the plain text? ")
    # shift = int(input("What is the shift? "))
    print("'help()' to receive help.")

    ask = input("\n] ")
    while ask != "quit()":
        if ask == "encrypt":
            plain_text1 = input("What is the plain text? ")
            shift1 = int(input("What is the shift? "))
            print("Message = <" + encrypt(plain_text1, shift1) + ">")
        elif ask == "decrypt":
            plain_text2 = input("What is the plain text? ")
            shift2 = int(input("What is the shift? "))
            print("Message = <" + decrypt(plain_text2, shift2) + ">")
        elif ask == "help()":
            print("-To encrypt, type: 'encrypt' \n-To decrypt, type: 'decrypt'")
        else:
            print("No known keyword " + ask)
        ask = input("\n] ")


if __name__ == "__main__":
    main()
