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
    n, k = invr()
    scores = inlt()
    total = 0
    for s in scores:
        if s >= scores[k - 1] and s > 0:
            total += 1
        else:
            break
    print(total)
