# Lockboxes

This project determines whether a set of numbered, interlocking boxes
can all be unlocked, starting from box 0 which is always open.

## Files

| File | Description |
| --- | --- |
| `0-lockboxes.py` | `canUnlockAll(boxes)`: returns `True` if every box can be opened using the keys found while exploring from box 0, `False` otherwise. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)

## Example

```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
```

Output:

```
True
```
