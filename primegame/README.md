# Prime Game

Maria and Ben take turns picking a prime from `1..n` and removing it with all
its multiples. The player who can't move loses. Find who wins the most of `x`
rounds when both play optimally.

## Files

| File | Description |
| --- | --- |
| `0-prime_game.py` | `isWinner(x, nums)`: returns `"Maria"`, `"Ben"`, or `None` on a tie |

## How it works

Each move removes exactly one prime, because the multiples of a prime are never
prime. So every round lasts as many moves as there are primes up to `n`, no
matter which primes are picked. Maria moves first, so she wins when that count
is odd and Ben wins when it is even.

One sieve of Eratosthenes up to the largest `n` builds a running count of
primes, and each round is then a single lookup.

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)
- No imports

## Example

```
$ ./main_0.py
Winner: Ben
```
