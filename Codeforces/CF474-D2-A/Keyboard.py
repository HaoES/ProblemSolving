#!/usr/bin/env python3
import sys

############ ---- Input Functions, coutery of 'thekushalghosh' ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s)]))


def invr():
    return(map(int, input().split()))


if __name__ == "__main__":
    way = input()
    word = insr()
    keyboard = list('qwertyuiopasdfghjkl;zxcvbnm,./')
    output = []
    if way == 'R':
        for w in word:
            output.append(keyboard[keyboard.index(w) - 1])
    if way == 'L':
        for w in word:
            output.append(keyboard[keyboard.index(w) + 1])

    print(''.join(output))
