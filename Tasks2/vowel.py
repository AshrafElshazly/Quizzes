def vowel(word):
    vowel = ['a','e','i','o','u']
    count = {x:sum([1 for char in word if char == x]) for x in vowel}
    return count

print(vowel('ashoiise'))