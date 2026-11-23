#!/usr/bin/python3


def count_primes_up_to(limit):
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
