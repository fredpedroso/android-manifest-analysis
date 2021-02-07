#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Decompile APK module. """

import logging
import tempfile
import os
from os import listdir
from source.settings import (
    DATABASE_DIR,
    TOOLS_DIR,
    APKTOOL_JAR
)

def decompile_apk(apk_path):
    """
    Decompile android application

    @param apk_path: Apk path <file or folder>
    @type  apk_path: str

    @return: An boolean:
                True: Apk decompiled successful
                False: Failed to decompile the apk file
    @rtype: bool
    """
    status = False
    if os.path.isdir(apk_path):
        apk_files = find_apk_filenames(apk_path)
        for apk_file in apk_files:
            status = decompile_cmd(apk_file, apk_path)

    elif os.path.isfile(apk_path):
        status = decompile_cmd(apk_path)

    else:
        logging.error('Could not find the file or directory %s', apk_path)

    return status


def decompile_cmd(apkfile_path, root_path=None):
    """
    Run decompile command

    @param apkfile_path: Apk file path
    @type  apkfile_path: str

    @param root_path: Root path of an apk file
    @type  root_path: str

    @return: An boolean:
                True: Apk decompiled successful
                False: Failed to decompile the apk file
    @rtype: bool
    """
    # full path of an apk file
    apktool_path = os.path.join(TOOLS_DIR, APKTOOL_JAR)
    if root_path:
        apkfile_path = root_path + '/' + apkfile_path

    # decompile the apk file
    status = False
    if os.path.isfile(apktool_path):
        # apktool command
        apk_foldername = os.path.basename(os.path.normpath(apkfile_path))
        decompiled_path = DATABASE_DIR + '/' + apk_foldername
        cmd_apktool_decompile = 'java -jar ' + \
            apktool_path + \
            ' --match-original' + \
            ' --frame-path ' + \
            tempfile.gettempdir() + \
            ' -f' + \
            ' -s' + \
            ' d ' + \
            apkfile_path + \
            ' -o' + \
            decompiled_path

        # execute the apktool command
        if os.system(cmd_apktool_decompile) == 0:
            status = True
        else:
            logging.error('Decompiling the apk file: %s', apkfile_path)
    else:
        logging.error('Could not find the apktool file: %s', apktool_path)

    return status


def find_apk_filenames(directory):
    """
    Find all apk filenames from a directory

    @param directory: Directory containing apks files
    @type  directory: str

    @return: List of apk filename of a directory
    @rtype: list
    """
    filenames = listdir(directory)
    extension = ".apk"
    return [filename for filename in filenames if filename.endswith(extension)]
