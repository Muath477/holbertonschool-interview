# Minimum Operations

This project finds the fewest operations needed to make a text file contain
exactly `n` copies of the character `H`, starting from a single `H`. The only
operations allowed are Copy All and Paste.

## Files

| File | Description |
| --- | --- |
| `0-minoperations.py` | `minOperations(n)`: returns the fewest operations to reach `n` H's, or `0` if `n` is impossible. It sums the prime factors of `n`. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)

## Example

```python
#!/usr/bin/python3
minOperations = __import__('0-minoperations').minOperations

print(minOperations(9))
```

Output:

```
6
```
