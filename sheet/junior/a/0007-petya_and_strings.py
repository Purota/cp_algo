#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def petya_and_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return -1

s1 = input()
s2 = input()
ans = petya_and_strings(s1, s2)
print(ans)
