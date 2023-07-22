

#with open("ten_words.txt",'r') as f:
t = int(input())
for i in range(t):
    n = int(input())
    highest = 0
    winner = None
    for j in range(n):
        words,quality = [int(x) for x in input().split()]
        if words>10:
            continue
        if quality > highest:
            highest = quality
            winner= j + 1
    print(winner)