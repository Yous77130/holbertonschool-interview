#!/usr/bin/python3
"""Module for UTF-8 validation."""


def validUTF8(data):
    """Determine if a data set represents a valid UTF-8 encoding."""
    n_bytes = 0

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
