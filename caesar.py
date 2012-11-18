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

def key_length(key):
    """Validate key length"""
    key = int(key)
    if key < 1 or key > 26:
        argparse.ArgumentTypeError("key must beetween 1 and %s " % (str(MAX_SHIFT_SIZE)))
    return key

def getParser():
    """Configure params"""
    parser = argparse.ArgumentParser(description='Encrypt/decrypt text with Caesar cipher')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')

    parser.add_argument('-k', '--key', help='key length [1..' + str(MAX_SHIFT_SIZE) + ']', required=True, type=key_length)

    parser.add_argument('data', nargs='?', help='data to encrypt/decrypt')
    parser.add_argument('--input', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='data to encrypt/decrypt (stdin)')
    return parser

if __name__ == "__main__":
    parser = getParser()
    try:
        args = parser.parse_args()
        data = args.data
        data_stdin = args.input

        if not data and not data_stdin:
            raise ValueError("no data specified")

        process_data = data if data else data_stdin.read().rstrip()

        mode = MODE_DECRYPT if args.decrypt else MODE_ENCRYPT
        print(translate(process_data, args.key, mode))
    except KeyboardInterrupt as e:
        pass
    except Exception as e:
        print("Error: %s" % (e))
