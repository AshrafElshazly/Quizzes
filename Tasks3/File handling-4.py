def cnt_words(fileName):
    f = open(fileName)
    data = f.read()
    print(len(data.split()))

cnt_words("Tasks3/f1.txt")