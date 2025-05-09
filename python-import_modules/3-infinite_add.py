#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        argument = int(sys.argv[i])
        result = result + argument
    print(result)
