#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Settings module. """

import logging
import os

# Directories
HOME = os.getcwd()                              # home
DATABASE_DIR = os.path.join(HOME, 'database/')  # database
TEMPLATE_DIR = os.path.join(HOME, 'template/')  # template
REPORT_DIR = os.path.join(HOME, 'report/')      # report
TOOLS_DIR = os.path.join(HOME, 'tools/')        # tools

# Report template
REPORT_TEMPLATE = os.path.join(TEMPLATE_DIR, 'manifest_analysis_template.xlsx')

# Tools
APKTOOL_JAR = 'apktool_2.5.0.jar'


def config_logging():
    """
    Logging format
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
