#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def strange_functions(n):
    return len(str(n))

t = int(input())
for _ in range(t):
    n = int(input())
    ans = strange_functions(n)
    print(ans)