from itertools import combinations

def find_triplets(arr):
    for i,v in enumerate(arr):
        for j in range(i+1,len(arr)):
            for k in range(j + 1,len(arr)):
                if v+arr[j]+arr[k] == 0:
                    print(v,w,x)
                    return 1
    return 0

print(find_triplets([4, -16, 43, 4, 7, -36, 18]))