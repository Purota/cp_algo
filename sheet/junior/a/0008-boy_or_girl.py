#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def boy_or_girl(s):
    s = set(s)
    if len(s) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

s = input()
ans = boy_or_girl(s)
print(ans)
