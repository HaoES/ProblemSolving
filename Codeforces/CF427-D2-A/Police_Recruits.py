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
    n = inp()
    events = inlt()
    cops = 0
    crimes = 0
    for i in events:
        if i > 0:
            cops += i
        else:
            if cops < 1:
                crimes += 1
            if cops > 0:
                cops -= 1
    print(crimes)
