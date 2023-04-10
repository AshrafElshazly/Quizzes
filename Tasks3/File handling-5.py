with open('Tasks3/file3.txt', 'r') as fr:
    lines = fr.readlines()
    flg = 1
    with open('Tasks3/file3.txt', 'w') as fw:
        for line in lines:
            if flg not in [3,4,5,6]:
                fw.write(line)
            flg += 1
print("Lines 3,4,5,6 have been deleted")
