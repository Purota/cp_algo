#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def smartphone_addiction(battery, time, a, b, N):
    battery = max(battery - (a - time), 0)
    if battery == 0:
        return battery
    return min(battery + (b - a), N)

N, M, T = map(int, input().split())
battery = N
time = 0
for _ in range(M):
    a, b = map(int, input().split())
    battery = smartphone_addiction(battery, time, a, b, N)
    time = b
    if battery == 0:
        break
ans = 'No'
battery = max(battery - (T - time), 0)
if battery > 0:
    ans = 'Yes'
print(ans)