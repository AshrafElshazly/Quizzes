#!/bin/python

import subprocess

def package():
    pckg = input("Enter Pachage Name: ")
    action = input("(install/remove): ")
    if action == "install" or action == "remove":
        subprocess.run(['yum',action,'-y',pckg])
    else:
        print("Sorry, I did not understand the action! ")
        
package()