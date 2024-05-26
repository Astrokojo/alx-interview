#!/usr/bin/python3
"""
UTF-8 Validator
"""


def validUTF8(data):
    """Checks if a given data
    set represents a valid UTF-8 encoding
    """

    bytes_left = 0
    for n in data:
        byte = format(n, '#010b')[-8:]
        if bytes_left == 0:
            if byte[0] == '1':
                bytes_left = len(byte.split('0')[0])
            if bytes_left > 4 or bytes == 1:
                return False
            if bytes_left == 0:
                continue
        else:
            if not byte.startswith('10'):
                return False
        bytes_left -= 1
    return bytes_left == 0
