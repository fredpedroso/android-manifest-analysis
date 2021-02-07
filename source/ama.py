#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Main Module. """

import logging
from source.settings import config_logging
from source.decompile import decompile_apk
from source.arguments import parse_args
from source.manifest_analysis import manifest_analysis
from source import __version__

def main():
    """
    Android Manifest Analysis (AMA) main
    """
    # configure logging
    config_logging()

    # input arguments
    args = parse_args()
    if args.path is not None:
        decompile_apk(args.path)
        manifest_analysis()
    elif args.version:
        logging.info('AMA version %s', __version__)
