#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sereja_and_dima(c, n):
    s = d = 0
    s_turn = n % 2
    while n > 0:
        c_n = c[0]
        i = 0
        if c_n < c[-1]:
            c_n = c[-1]
            i = -1
        c.pop(i)
        if n % 2 == s_turn:
            s += c_n
        else:
            d += c_n
        n -= 1
    return s, d
            

n = int(input())
c = [int(c_i) for c_i in input().split()]
ans = sereja_and_dima(c, n)
print(*ans)
