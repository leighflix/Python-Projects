import math


def trans_encrypt(message, n):
    return "".join([message[i::n] for i in range(n)])


def trans_decrypt(cipher, n):
    length = math.ceil(len(cipher) / n)
    message = ''
    for i in range(length):  # length = 3, n = 2
        for j in range(n):
            letter = (i + j * length)
            if letter == len(cipher):
                message += ''
            else:
                message = message + cipher[letter]
    return message
