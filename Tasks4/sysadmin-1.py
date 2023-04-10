#!/bin/python

import subprocess

def ping():
    target = input("Enter Destination Name: ")
    if target:
        subprocess.run(['ping',target])
        
ping()