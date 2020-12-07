#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def stones_on_the_table(s):
    last = ''
    count = 0
    for c in s:
        if c == last:
            count += 1
        last = c
    return count

n = int(input())
s = input()
ans = stones_on_the_table(s)
print(ans)
