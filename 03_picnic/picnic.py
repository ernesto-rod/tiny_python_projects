#!/usr/bin/env python3
"""
Author: Ernesto Antonio Rodriguez <ernesto.antonio.rod@gmail.com>
Date   : 2023-10-18
Purpose: 03_picnic/picnic.py
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    msg = str()
    if num == 1:
        msg = items[0]
    elif num == 2:
        msg = ' and '.join(items)
    elif num > 2:
        msg = f"{', '.join(items[:-1])}, and {items[-1]}"

    print(f'You are bringing {msg}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
