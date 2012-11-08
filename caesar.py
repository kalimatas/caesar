#!/usr/bin/env python

import sys
import argparse

# only English alphabet
MAX_SHIFT_SIZE = 26
MODE_ENCRYPT='e'
MODE_DECRYPT='d'

def translate(input, key, mode=MODE_DECRYPT):
    """Encrypt/dectypt input"""
    if key < 1 or key > 26:
        raise ValueError("key must beetween 1 and %s " % (str(MAX_SHIFT_SIZE)))

    import string
    shifted_chars = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    if mode == MODE_ENCRYPT:
        return input.translate(str.maketrans(string.ascii_lowercase, shifted_chars))
    elif mode == MODE_DECRYPT:
        return input.translate(str.maketrans(shifted_chars, string.ascii_lowercase))
    else:
        raise ValueError("unknown mode: %s" %s (mode))

def getParser():
    """Configure params"""
    parser = argparse.ArgumentParser(description='Encrypt/dectypt text with Caesar cipher')
    parser.add_argument('-k', '--key', help='key length [1..' + str(MAX_SHIFT_SIZE) + ']', required=True, type=int)
    parser.add_argument('-i', '--input', help='data to encrypt/decrypt', required=True)
    return parser

if __name__ == "__main__":
    parser = getParser()
    args = parser.parse_args()
    try:
        print(translate(args.input, args.key))
    except Exception as e:
        print("Error: %s" % (e))
