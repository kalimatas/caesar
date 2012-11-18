#!/usr/bin/env python

import sys
import argparse

# only English alphabet
MAX_SHIFT_SIZE = 26
MODE_ENCRYPT='e'
MODE_DECRYPT='d'

def translate(input, key, mode=MODE_ENCRYPT):
    """Encrypt/decrypt input"""
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
    parser = argparse.ArgumentParser(description='Encrypt/decrypt text with Caesar cipher')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')

    parser.add_argument('-k', '--key', help='key length [1..' + str(MAX_SHIFT_SIZE) + ']', required=True, type=int)
    parser.add_argument('data', help='data to encrypt/decrypt')
    return parser

if __name__ == "__main__":
    parser = getParser()
    args = parser.parse_args()
    try:
        mode = MODE_DECRYPT if args.decrypt else MODE_ENCRYPT
        print(translate(args.data, args.key, mode))
    except Exception as e:
        print("Error: %s" % (e))
