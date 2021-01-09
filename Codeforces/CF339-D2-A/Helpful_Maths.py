#!/usr/bin/env python3
import sys
input = sys.stdin.readline

############ ---- Input Functions, coutery of 'thekushalghosh' ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split('+'))))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


if __name__ == "__main__":
    sum = inlt()

    def bubsort(list):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(list) - 1):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    swapped = True
    bubsort(sum)
    sortedsum = [str(i) for i in sum]
    print('+'.join(sortedsum))
