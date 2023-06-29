ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def encode(word,newalpha):
    """Changes words in newalpha to regular alpha"""
    output = ''
    for i,v in enumerate(word):
        output += ALPHA[newalpha.index(v)]
    return output

def isAlienSorted(words,order,testing=False):
    if testing:
        print("words:",words)
    newwords = [encode(w,order) for w in words]
    if testing:
        print("newwords:",newwords)
    return newwords == sorted(newwords)


print(isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz",True))