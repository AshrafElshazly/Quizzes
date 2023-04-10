#!/bin/python

import subprocess

def excMod(file):
    subprocess.run(['chmod','771', file])

def handle():
    subprocess.run(['mkdir','newdir'])
    subprocess.run(['touch','newdir/newfile'])
    excMod('newdir/newfile')

handle()