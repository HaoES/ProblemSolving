#!/usr/bin/env python3
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


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
    games = insr()
    countA, countD = games.count('A'), games.count('D')
    # Using the string count method is faster than looping through the entire list
    if countA == countD:
        print('Friendship')
    if countD > countA:
        print('Danik')
    if countA > countD:
        print('Anton')
