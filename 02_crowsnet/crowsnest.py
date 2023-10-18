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
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    vowels = 'aeiou'

    article = 'an' if word[0].lower() in vowels else 'a'
    print(f'Ahoy, Captain, {article} {word} off the lardboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
