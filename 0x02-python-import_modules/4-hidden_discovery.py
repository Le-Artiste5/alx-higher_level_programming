#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    compmodf = dir()
    for i in range(0, len(compmodf)):
        if compmodf[i][:2] != "__":
            print("{:s}".format(compmodf[i]))
