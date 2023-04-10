#!/bin/python

import subprocess

def multiTouch():
    files = [input(f'Enter name of file number {i}: ') for i in range(1,6)]
    for i in range(len(files)):
        subprocess.run(['touch',files[i]])

multiTouch()
