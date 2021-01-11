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
    first = insr()
    second = insr()
    flag = False
    if len(first) == len(second):
        flag = True
        for i, j in zip(first, second):
            if i != j:
                flag = False
                break

    if flag:
        print(-1)
    else:
        print(max(len(first), len(second)))
