# N Queens

The N queens puzzle: place N non-attacking queens on an N x N chessboard. The program prints every solution, one per
line, as a list of `[row, column]` pairs.

## Files

| File | Description |
| --- | --- |
| `0-nqueens.py` | `nqueens N`: solves the puzzle with backtracking. Prints `Usage: nqueens N`, `N must be a number` or `N must be at least 4` and exits with status 1 on bad input. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)
- Only the `sys` module is imported

## Example

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
