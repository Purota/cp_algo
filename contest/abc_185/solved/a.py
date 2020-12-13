#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def abc_preparation(a):
    return min(a)

a = [int(a_i) for a_i in input().split()]
ans = abc_preparation(a)
print(ans)