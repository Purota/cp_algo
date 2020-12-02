#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Input:
    The first line contains one integer t - the number of test cases
    The first line of each test case contains two integers N - the array size - and V the target
    The second line of each test case contains a sorted array of integers separated by a space
Output:
    The index of the target if it is present in the array, else -1
"""

t = int(input())

def binary_search(A, target):
    low = 0
    high = len(A) - 1
    while low < high:
        mid = (low + high) // 2
        value = A[mid]
        if value == target:
            return mid
        elif value > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

for _ in range(t):
    N, V = map(int, input().split())
    arr = [int(x) for x in input().split()]
    ind = binary_search(arr, V)
    print(ind)
