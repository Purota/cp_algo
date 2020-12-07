#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gravity_flip(a):
    return sorted(a)

n = int(input())
a = [int(a_i) for a_i in input().split()]
ans = gravity_flip(a)
print(*ans)
