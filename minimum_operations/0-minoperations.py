#!/usr/bin/python3
"""Calculate the fewest operations needed to produce n H characters."""


def minOperations(n):
    """Return the fewest Copy All and Paste operations that yield n H's.

    Each prime factor p of n costs p operations (one Copy All and p - 1
    pastes), because it multiplies the current length by p. So the answer
    is the sum of the prime factors of n.

    Args:
        n (int): The number of H characters to reach.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
