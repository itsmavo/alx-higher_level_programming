#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = sum(int(sys.argv[i]) for i in range(1, len(sys.argv)))
    print("{}".format(result))
