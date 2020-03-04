#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "mprodhan/yabamov"


# +++your code here+++
# Write functions and modify main() to call them


def special_paths(dir):
    result_path = []
    paths = os.listdir(dir)
    for file in paths:
        file_match = re.search(r'__(\w+)__', file)
        if file_match:
            match_path = os.path.abspath(os.path.join(dir, file))
            result_path.append(match_path)
    return result_path


def copy_to(paths, dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)
    for file in paths:
        dest_file = os.path.join(dir, os.path.basename(file))
        print('copying source = {} dest_file = {} '.format(file, dest_file))
        shutil.copy(file, dest_file)


def zip_to(paths, zippath):
    cmd = ['zip', '-j', zippath]
    cmd.extend(paths)
    print("Command I'm going to execute: ")
    print(cmd)
    output = subprocess.check_output(cmd)
    print(output)

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='able to call directories')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdlines.
    # Read the docs and examples for the argparse module about how to do this.
    from_dir = args.from_dir
    copy_dir = args.todir
    zip_dir = args.tozip

    special_paths_ = special_paths(from_dir)

    if copy_dir:
        copy_to(special_paths_, copy_dir)
    elif zip_dir:
        zip_to(special_paths_, zip_dir)
    else:
        print(special_paths_)


    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
