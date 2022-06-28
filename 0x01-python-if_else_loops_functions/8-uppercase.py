#!/usr/bin/python3

def uppercase(str):
    special_chars = " ,-_@^*&%$!"
    for i in str:
        ascii = ord(i)
        if i not in special_chars:
            if ascii >= 97:
                ascii = ascii - 32
        print("{0:i}".format(ascii), end="")
    print()
