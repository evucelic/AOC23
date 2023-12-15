from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split(",")


def HASH(string: str) -> int:
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current = current % 256

    return current


def main():
    res = 0
    for d in D:
        res += HASH(d)
    print(res)


if __name__ == "__main__":
    main()
