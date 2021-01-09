#!/usr/bin/env python3
import sys
input = sys.stdin.readline

############ ---- Input Functions, coutery of 'thekushalghosh' ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


if __name__ == "__main__":
    n, b, d = invr()
    oranges = inlt()
    oranges = [o for o in oranges if o <= b]
    count = 0
    dumps = 0
    for o in oranges:
        count += o
        if count > d:
            dumps += 1
            count = 0
    print(dumps)
