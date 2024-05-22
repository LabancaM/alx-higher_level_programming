#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0")
    else:
        sum = 0
        for i in sys.argv[1:]:
            sum += int(i)
        print("{}".format(sum))
