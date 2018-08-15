#! /usr/bin/env python3

prefix = "/home/prj/"

import os

for n in range(40):
    name = prefix + "{:02}".format (n)
    os.mkdir (name)
