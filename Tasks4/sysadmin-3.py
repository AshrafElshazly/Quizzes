#!/bin/python

import subprocess

def check():
    pckg = input("Enter Package Name: ")
    res = subprocess.run(['rpm','-q',pckg],capture_output=True)
    if res.returncode == 0 : 
        print("Package " ,pckg," is already installed")
    else :
        subprocess.run(['yum','install','-y',pckg])

check()