# Making Change

Given coins of different values (as many of each as needed), find the fewest
coins that add up to a total.

## Files

| File | Description |
| --- | --- |
| `0-making_change.py` | `makeChange(coins, total)`: bottom-up dynamic programming over every amount from 0 to `total`. Returns `0` when `total <= 0` and `-1` when the total can't be reached. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)

## Example

```
$ ./0-main.py
7
-1
```

Runs in `O(len(coins) * total)` time and `O(total)` memory.
