#!/usr/bin/python3

def islower(x):
    ascii = ord(x)
    if (ascii < 97 or ascii > 122):
        return False
    return True
