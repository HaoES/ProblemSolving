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
    snacks = inlt()
    flag = [False] * (n + 1)
    for snack in snacks:
        flag[snack] = True
        if snack == n:
            while flag[n]:
                print(n, end=' ')
                n -= 1
        print()
