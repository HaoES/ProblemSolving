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


def pickcard(c):
    if len(c) == 0:
        return [], 0
    if c[0] > c[-1]:
        a = c[0]
        c.pop(0)
        return c, a
    else:
        a = c[-1]
        c.pop()
        return c, a


if __name__ == "__main__":
    n = int(input())
    cards = inlt()
    sums, sumd = 0, 0
    while len(cards):
        cards, a = pickcard(cards)
        sums += a
        cards, b = pickcard(cards)
        sumd += b
    print(str(sums) + ' ' + str(sumd))
