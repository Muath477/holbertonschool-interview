# UTF-8 Validation

This project checks whether a list of integers is a valid UTF-8 encoding. A character in UTF-8 is 1 to 4 bytes long, and
each integer of the list represents one byte (only its 8 least significant bits are used).

## Files

| File | Description |
| --- | --- |
| `0-validate_utf8.py` | `validUTF8(data)`: returns `True` if `data` is a valid UTF-8 encoding, `False` otherwise. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)

## How it works

The first byte of a character tells how many bytes it has:

| First byte | Bytes in the character |
| --- | --- |
| `0xxxxxxx` | 1 |
| `110xxxxx` | 2 |
| `1110xxxx` | 3 |
| `11110xxx` | 4 |

Every other byte of the character must start with `10`. The function walks the list once and keeps track of how many
continuation bytes are still expected.

## Example

```python
#!/usr/bin/python3
validUTF8 = __import__('0-validate_utf8').validUTF8

print(validUTF8([65]))
print(validUTF8([229, 65, 127, 256]))
```

Output:

```
True
False
```
