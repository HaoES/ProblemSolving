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
    ri = 0
    ci = 0
    for i in range(5):
        a = inlt()
        if 1 in a:
            ri = i+1
            ci = a.index(1) + 1
    swaps = abs(3 - ri) + abs(3 - ci)
    print(swaps)
