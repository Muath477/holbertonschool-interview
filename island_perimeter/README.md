# Island Perimeter

Find the perimeter of the single island in a grid where `1` is land and `0`
is water.

## Files

| File | Description |
| --- | --- |
| `0-island_perimeter.py` | `island_perimeter(grid)`: adds 4 for each land cell and takes away 2 for each side shared with the land cell above or to the left |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7)
- No modules imported

## Example

```
$ ./0-main.py
12
```

Runs in `O(rows * columns)` time, which is at most 10,000 cells for a 100 x 100 grid.
