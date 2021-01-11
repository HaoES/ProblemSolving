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
    cities = inlt()
    for i in range(n):
        if i == 0:
            print(cities[i+1] - cities[i], abs(cities[i] - cities[-1]))
        elif i == n - 1:
            print(cities[i] - cities[i-1], abs(cities[i] - cities[0]))
        else:
            print(min(abs(cities[i] - cities[i-1]), abs(cities[i+1] - cities[i])),
                  max(abs(cities[i] - cities[0]), abs(cities[i] - cities[-1])))
