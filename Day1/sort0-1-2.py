from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def sort012(arr, n):
    zeroes = 0
    ones = 0
    for ele in arr:
        if ele == 0:
            zeroes += 1
        elif ele == 1:
            ones += 1
    for i in range(n):
        if zeroes:
            arr[i] = 0
            zeroes -= 1
        elif ones:
            arr[i] = 1
            ones -= 1
        else:
            arr[i] = 2
# taking inpit using fast I/O


def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):

    for i in range(n):

        print(arr[i], end=" ")

    print()

# main


t = int(input().strip())
for i in range(t):

    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
