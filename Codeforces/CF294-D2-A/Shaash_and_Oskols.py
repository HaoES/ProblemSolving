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
    def shot(l, a, b):
        a -= 1
        if len(l) == 1:
            return [0]
        if a == 0:
            l[a+1] += l[a] - b
            l[a] = 0
            return l
        if a == len(l) - 1:
            l[a-1] += b - 1
            l[a] = 0
            return l
        else:
            l[a-1] += b - 1
            l[a+1] += l[a] - b
            l[a] = 0
            return l
    n = inp()
    wires = inlt()
    m = inp()
    for i in range(m):
        a, b = invr()
        wires = shot(wires, a, b)
    for w in wires:
        print(w)
