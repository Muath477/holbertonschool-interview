# Log Parsing

This project reads an access log from standard input, line by line, and
prints running statistics.

## Files

| File | Description |
| --- | --- |
| `0-stats.py` | Reads lines like `<IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>` and prints the cumulative total file size and the number of lines per status code (200, 301, 400, 401, 403, 404, 405, 500). Lines in another format are skipped for the statistics. The stats are printed every 10 lines and on CTRL + C. |

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code style checked with `pycodestyle` (1.7.x)

## Example

```
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
301: 3
```
