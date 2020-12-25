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
    n = int(input())
    count = 1
    numbers = []
    for i in range(n):
        numbers.append(inlt())
    count += sum([numbers[i] != numbers[i+1] for i in range(n-1)])
    print(count)
