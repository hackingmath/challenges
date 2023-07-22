from itertools import combinations

def lowest(a,b):
    if a == 0 or b == 0:
        return True
    if a / b not in [1,-1]:
        print(a,b)
        return False
    return True

def align(arr):
    pairs = 0
    for pair in combinations(arr,2):
        x,y = pair[0][0]-pair[1][0],pair[0][1]-pair[1][1]
        if lowest(x,y):
            pairs += 1
    return pairs

with open("star.txt",'r') as f:
    t = int(f.readline())
    for i in range(t):
        n=int(f.readline())

        stars = list()
        for i in range(n):
            stars.append([int(x) for x in f.readline().split()])

        print(align(stars)*2)