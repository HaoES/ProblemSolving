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
    k, r = invr()
    count = 1
    price = baseprice = k
    while (price % 10 != r) and (price % 10 != 0):
        count += 1
        price += baseprice
    print(count)
