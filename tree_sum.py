#Sum in Binary Tree
# https://codeforces.com/problemset/problem/1843/C
# July 9, 2023

def tree_sum(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return n + tree_sum(n//2)
    else:
        return n + tree_sum((n-1)//2)

tests = [3,10,37,1,10000000000000000,15]

for i in tests:
    print(i,tree_sum(i))

# T = int(input())
# for i in range(T):
#     print(tree_sum(int(input())))