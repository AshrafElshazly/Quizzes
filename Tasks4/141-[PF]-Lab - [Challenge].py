#!/bin/python

for n in range(255):
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                break
        else:    
            file1 = open("Tasks4/prime.txt", "a")
            file1.write(f"{n} \n")
