#!/usr/bin/python3
"""Script to solve the coin change problem"""


def makeChange(coins, total):
    """Script to solve the coin change problem"""
    subs = [total + 1] * (total + 1)
    subs[0] = 0
    for i in range(1, total + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                subs[i] = min(subs[i], subs[i - coins[j]] + 1)

    return -1 if subs[total] > total else subs[total]
