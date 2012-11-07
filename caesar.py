#!/usr/bin/env python

import sys
import argparse
import string

# only English alphabet
MAX_SHIFT_SIZE = 26

def translate(input, key):
    raise ValueError("key must beetween 1 and %s " % (str(MAX_SHIFT_SIZE)))

def getParser():
    parser = argparse.ArgumentParser(description='Encrypt/dectypt text with Caesar cipher')
    return parser

if __name__ == "__main__":
    parser = getParser()
    parser.add_argument('-k', '--key', help='key length [1..' + str(MAX_SHIFT_SIZE) + ']', required=True, type=int)
    parser.add_argument('-i', '--input', help='data to encrypt/decrypt', required=True)
    args = parser.parse_args()
    try:
        print(translate(args.input, args.key))
    except Exception as e:
        print("Error: %s" % (e))
        pass