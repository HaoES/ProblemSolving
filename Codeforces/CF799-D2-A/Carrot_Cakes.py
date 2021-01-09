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
    n, t, k, d = invr()

    def twoOvens(d):
        o1 = 0
        o2 = -d
        duration = 0
        cake = 0
        while True:
            duration += 1
            o1 += 1
            o2 += 1
            if o1 % t == 0:
                cake += k
                if cake == n:
                    return duration
            if o2 % t == 0 and o2 > 0:
                cake += k
                if cake >= n:
                    return duration

    def oneOven():
        o1 = 0
        duration = 0
        cake = 0
        while True:
            duration += 1
            o1 += 1
            if o1 % t == 0:
                cake += k
                if cake >= n:
                    return duration
    one = oneOven()
    two = twoOvens(d)
    if two < one:
        print('YES')
    else:
        print('NO')
