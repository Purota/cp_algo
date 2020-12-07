#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def buy_a_shovel(k, r):
    count = 1
    rem = k % 10 
    while rem != r and rem != 0:
        count += 1
        rem = (count * k) % 10
    return count

k, r = map(int, input().split())
ans = buy_a_shovel(k, r)
print(ans)
