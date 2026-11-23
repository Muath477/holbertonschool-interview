#!/usr/bin/python3
"""Find the winner of the prime game over several rounds."""


def count_primes_up_to(limit):
    """Return a list where index n holds how many primes are <= n."""
    is_prime = [False, False] + [True] * (limit - 1)
    number = 2
    while number * number <= limit:
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
        number += 1

    counts = [0] * (limit + 1)
    for number in range(1, limit + 1):
        counts[number] = counts[number - 1] + is_prime[number]
    return counts


def isWinner(x, nums):
    """Return "Maria" or "Ben", whoever wins the most of the x rounds.

    Every move removes exactly one prime, so a round has as many moves as
    there are primes up to n. Maria starts, so she wins when that count is
    odd. Returns None when both win the same number of rounds.
    """
    if x < 1 or not nums:
        return None

    rounds = nums[:x]
    prime_counts = count_primes_up_to(max(max(rounds), 1))

    maria_wins = 0
    for n in rounds:
        if n > 1 and prime_counts[n] % 2 == 1:
            maria_wins += 1
    ben_wins = len(rounds) - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
