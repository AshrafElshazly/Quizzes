def dup(string):
    res=''
    for i in range(0, len(string)):
        res += string[i]+ string[i]
    return res
    
print(dup('ashraf'))
