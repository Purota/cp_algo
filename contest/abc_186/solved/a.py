#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def brick(n, w):
    return n // w

n, w = map(int, input().split())
ans = brick(n, w)
print(ans)