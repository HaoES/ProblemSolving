#!/usr/bin/env python3
import sys
input = sys.stdin.readline

############ ---- Input Functions, coutery of 'thekushalghosh' ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(input().split()))


def insr():
    s = input()
    return(list(s[:len(s)]))


def invr():
    return(map(int, input().split()))


if __name__ == "__main__":
    n, x = invr()
    c = 0
    for i in range(n):
        visitor = inlt()
        if visitor[0] == '+':
            x += int(visitor[1])
        if visitor[0] == '-':
            if int(visitor[1]) > x:
                c += 1
            else:
                x -= int(visitor[1])
    print(str(x) + ' ' + str(c))
