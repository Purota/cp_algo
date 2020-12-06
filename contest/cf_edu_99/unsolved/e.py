#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os
import itertools

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    
def four_points(P):
    min_cost = 4 * int(1e9)
    for p in itertools.permutations(range(4)):
        (ax, ay), (bx, by), (cx, cy), (dx, dy) = (P[i] for i in p)
        x1 = min(ax, bx), max(ax, bx)
        x2 = min(cx, dx), max(cx, dx)
        cost = x1[1] - x1[0] + x2[1] - x2[0]
        y1 = min(ay, cy), max(ay, cy)
        y2 = min(by, dy), max(by, dy)
        cost += y1[1] - y1[0] + y2[1] - y2[0]
        x_seg = max(x1[0] - x2[1], x2[0] - x1[1]), max(x1[1] - x2[0], x2[1] - x1[0])
        y_seg = max(y1[0] - y2[1], y2[0] - y1[1]), max(y1[1] - y2[0], y2[1] - y1[0])
        cost += 2 * max(0, max(x_seg[0], y_seg[0]) - min(x_seg[1], y_seg[1]))
        min_cost = min(min_cost, cost)
    return min_cost

t = int(input())
for _ in range(t):
    P = [[int(xy) for xy in input().split()] for _ in range(4)]
    ans = four_points(P)
    print(ans)