#!/usr/bin/env python3
import random
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
    letters = random.sample(range(97, 123), k)
    password = []
    for i in range(n):
        password.append(chr(letters[i % k]))
    print(''.join(password))
