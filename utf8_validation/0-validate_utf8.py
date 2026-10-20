#!/usr/bin/python3
"""Determine whether a data set is a valid UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else return False.

    A UTF-8 character is 1 to 4 bytes long. The first byte tells how many
    bytes follow (0xxxxxxx, 110xxxxx, 1110xxxx or 11110xxx) and each
    following byte must look like 10xxxxxx.

    Args:
        data (list): integers. Only the 8 least significant bits of each
            integer are used, as one byte.

    Returns:
        bool: True if the bytes form valid UTF-8 characters, else False.
    """
    expected = 0
    for number in data:
        byte = number & 0xFF
        if expected:
            if byte >> 6 != 0b10:
                return False
            expected -= 1
        elif byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            expected = 1
        elif byte >> 4 == 0b1110:
            expected = 2
        elif byte >> 3 == 0b11110:
            expected = 3
        else:
            return False
    return expected == 0
