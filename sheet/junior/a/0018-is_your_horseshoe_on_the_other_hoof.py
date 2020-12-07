#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_your_horseshoe_on_the_other_hoof(s):
    colors = set()
    count = 0
    for s_i in s:
        if s_i in colors:
            count += 1
        colors.add(s_i)
    return count

s = [int(s_i) for s_i in input().split()]
ans = is_your_horseshoe_on_the_other_hoof(s)
print(ans)
