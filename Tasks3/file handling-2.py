def cnt_out():
    f1 = open("Tasks3/f1.txt")
    count = 0
    for x in f1.read():
        if x.isupper(): count+=1
    f2 = open("Tasks3/f1-count.txt","w")
    f2.write(str(count))

cnt_out()