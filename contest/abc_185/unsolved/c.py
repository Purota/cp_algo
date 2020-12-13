#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def duodecim_ferra(L):
    L -= 1
    return math.factorial(L) // (math.factorial(11) * math.factorial(L - 11))

L = int(input())
ans = duodecim_ferra(L)
print(ans)