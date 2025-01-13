#!/usr/bin/env python3
"""
Author: Ernesto Antonio Rodriguez <ernesto.antonio.rod@gmail.com>
Date   : 2025-01-12
Purpose: gashlycrumb.py
"""

import argparse

from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="./gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    entries = {
            line[0].upper(): line.rstrip()
        for
            line
        in
            args.file
    }
    
    # pprint(entries)
    for letter in args.letter:
        if letter.upper() in entries:
            print(entries[letter.upper()])
        else:
            print(f'I do not know "{letter}".\n', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
