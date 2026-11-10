#!/usr/bin/python3
"""Find the fewest coins needed to reach a given total."""


def makeChange(coins, total):
    """Return the fewest coins that add up to total, or -1 if impossible.

    fewest[x] is the best count found so far for the amount x. Each amount
    is a smaller amount plus one coin, so building the table from 0 upward
    means every lookup on the right side is already final.
    """
    if total <= 0:
        return 0

    # an answer never needs more than total coins, so total + 1 = unreachable
    fewest = [0] + [total + 1] * total
    for coin in coins:
        for amount in range(coin, total + 1):
            if fewest[amount - coin] + 1 < fewest[amount]:
                fewest[amount] = fewest[amount - coin] + 1

    if fewest[total] > total:
        return -1
    return fewest[total]
