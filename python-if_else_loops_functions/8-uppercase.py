#!/usr/bin/python3
def uppercase(str):
    print("".join("{:c}".format(ord(c) - 32 if 'a' <= c <= 'z' else ord(c)) for c in str))
