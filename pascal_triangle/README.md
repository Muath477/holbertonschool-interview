# Pascal's Triangle

This project implements a function that builds Pascal's triangle up to a
given number of rows.

## Files

| File | Description |
| --- | --- |
| `0-pascal_triangle.py` | `pascal_triangle(n)`: returns a list of lists of integers representing Pascal's triangle up to row `n`, or `[]` if `n <= 0`. |

## Requirements

- Python 3
- Code style checked with `pycodestyle`

## Example

```python
#!/usr/bin/env python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

for row in pascal_triangle(5):
    print(row)
```

Output:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
