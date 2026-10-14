#!/usr/bin/python3
"""Read an access log from stdin and print running statistics."""
import re
import sys

STATUS_CODES = ("200", "301", "400", "401", "403", "404", "405", "500")
PRINT_EVERY = 10
LINE_FORMAT = re.compile(
    r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\S+) (\d+)$')


def print_stats(total_size, status_counts):
    """Print the total file size and the count of each status code seen."""
    print("File size: {}".format(total_size))
    for code in STATUS_CODES:
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line, printing the stats every 10 lines.

    The stats are cumulative since the first line. They are also printed
    when the input ends with a partial batch, or on CTRL + C.
    """
    total_size = 0
    status_counts = dict.fromkeys(STATUS_CODES, 0)
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            match = LINE_FORMAT.match(line.strip())
            if match:
                status, size = match.groups()
                total_size += int(size)
                if status in status_counts:
                    status_counts[status] += 1

            if lines_read % PRINT_EVERY == 0:
                print_stats(total_size, status_counts)

        if lines_read % PRINT_EVERY != 0:
            print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
