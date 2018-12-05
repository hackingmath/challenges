'''Broken Necklace Problem
December 6, 2018'''

import random

N_ZEROES = 34
N_ONES = 26

a = N_ZEROES*[0] + N_ONES*[1]
random.shuffle(a)

print(a)

def solve():
    #first check one slice
    s1 = int(len(a)/2)
    first_half = a[:s1]
    second_half = a[s1:]
    if first_half.count(0)==second_half.count(0):
        if first_half.count(1)==second_half.count(1):
            print("One slice:",s1)
            print(first_half,second_half)
    for s1 in range(1,len(a)-1):
        for s2 in range(s1,len(a)):
            p1 = a[:s1]
            p2 = a[s1:s2]
            p3 = a[s2:]

            first_half = p1 + p2
            second_half = p3
            if first_half.count(0)==second_half.count(0):
                if first_half.count(1)==second_half.count(1):
                    print(s1,s2)
                    print("p1 + p2 = p3")
                    print(p1,p2,p3)
                    #print(first_half,second_half)

            first_half = p1 + p3
            second_half = p2
            if first_half.count(0)==second_half.count(0):
                if first_half.count(1)==second_half.count(1):
                    print(s1,s2)
                    print("p1 + p3 = p2")
                    print(p1,p2,p3)

            first_half = p3 + p2
            second_half = p1
            if first_half.count(0)==second_half.count(0):
                if first_half.count(1)==second_half.count(1):
                    print(s1,s2)
                    print("p3 + p2 = p1")
                    print(p1,p2,p3)

solve()
