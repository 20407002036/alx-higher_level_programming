#!/usr/bin/python3
output = ''.join(chr(char_code) for char_code in range(ord('a'), ord('z') + 1))
if (char_code != 'e' and char_code != 'q'):
    print('{}'.format(output), end='')
