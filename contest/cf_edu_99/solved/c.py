#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ping_pong(x, y):
    return x - 1, y

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    ans = ping_pong(x, y)
    print(ans[0], ans[1])