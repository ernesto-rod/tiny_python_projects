#!/usr/bin/env python3
"""
Author: Ernesto Antonio Rodriguez <ernesto.antonio.rod@gmail.com>
Date   : 2023-10-05
Purpose: crowsnest.py
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    print('Ahoy, Captain, a ' + word + ' off the lardboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
