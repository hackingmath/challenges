import itertools

def over_ten(arr):
    for x in itertools.combinations(arr,2):
        if sum(x) >= 10:
            return True
    return False

t = int(input())
for i in range(t):
    arr = [int(x) for x in input().split()]
    if over_ten(arr):
        print("YES")
    else:
        print("NO")