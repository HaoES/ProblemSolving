#!/usr/bin/env python3
import itertools
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
    children = inlt()
    teams = min(children.count(1), children.count(2), children.count(3))
    ones = []
    twos = []
    threes = []
    for i in range(len(children)):
        if children[i] == 1:
            ones.append(i + 1)
        if children[i] == 2:
            twos.append(i + 1)
        if children[i] == 3:
            threes.append(i + 1)
    print(teams)
    for team in zip(ones, twos, threes):
        print(*team)
