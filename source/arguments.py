
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

""" Arguments Module. """


def parse_args():
    """
    Parse input arguments
    
    @return: Arguments
    @rtype: list
    """
    parser = argparse.ArgumentParser(description='Android Manifest Analysis')
    parser.add_argument('--path',
                        dest='path',
                        help='apk path <file or directory>',
                        type=str)
    parser.add_argument('--version',
                        dest='version',
                        action='store_true',
                        help='version')
    args = parser.parse_args()
    return args
