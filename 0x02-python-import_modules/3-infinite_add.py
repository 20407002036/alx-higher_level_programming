#!/usr/bin/python3
if __name__ == "__main__":
    #it add an infinite number trust me when I say that
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
