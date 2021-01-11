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
    coins = inlt()

    def reverse(list):
        if len(list) == 1:
            return list
        swap = True
        while swap:
            swap = False
            for i in range(len(list) - 1):
                if list[i] < list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    swap = True
        return list
    sortedcoins = reverse(coins)
    total = sum(sortedcoins)
    nbcoin = 0
    value = 0
    while value <= total//2:
        value += sortedcoins[nbcoin]
        nbcoin += 1
    print(nbcoin)
