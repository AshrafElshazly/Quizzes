def alpha():
    f = open("Tasks3/file2.txt")
    count = 0
    for x in f:
        if x[0] != 'T': count+=1
    print(count)

alpha()