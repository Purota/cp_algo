#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SRM 258 - AutoLoan
https://community.topcoder.com/stat?c=problem_statement&pm=3970&rd=7993

Input:
First line contains an integer t - the number of test cases
Each case test contains two floats p - the price -, m - the monthly payment - and an integer l - the loan term -
"""

def positive_balance(balance, monthly_payment, loan_term, rate):
    for _ in range(loan_term):
        balance += balance * rate - monthly_payment
    return balance >= 0.0

def interest_rate(price, monthly_payment, loan_term):
    low = 0.0
    high = 1.0
    while high - low > 1e-12:
        mid = (high + low) / 2
        if positive_balance(price, monthly_payment, loan_term, mid):
            high = mid
        else:
            low = mid
    return low * 12 * 100

t = int(input())

for _ in range(t):
    p, m, l = input().split()
    p, m, l = float(p), float(m), int(l)
    rate = interest_rate(p, m, l)
    print("{:.9f}".format(rate))