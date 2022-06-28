#!/usr/bin/python3
def magic_calculation(i, j, k):
    if i < j:
        return k
    else:
        if k > j:
            return i + j
        else:
            return i * j - k
