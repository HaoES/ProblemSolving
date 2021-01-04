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
    s = insr()
    order = [1] + [ord(i) - 96 for i in s]
    diffs = [abs(t - s) if abs(t-s) < 14 else 26 - abs(t-s)
             for s, t in zip(order, order[1:])]
    print(sum(diffs))
