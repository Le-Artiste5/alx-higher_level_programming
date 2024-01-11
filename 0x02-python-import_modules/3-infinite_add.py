#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sint = 0
    for i in range(1, len(argv)):
        sint += int(argv[i])
    print("{}".format(sint))
