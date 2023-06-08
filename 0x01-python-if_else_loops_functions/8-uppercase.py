#!/usr/bin/python3
def uppercase(s):
    for c in s:
        upper_c = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(upper_c), end='')
    print("\n",  end="")
