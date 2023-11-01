#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char_code)), end='')
