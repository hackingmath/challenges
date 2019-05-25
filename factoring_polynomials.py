"""Factoring Polynomials
May 22, 2019
From Hacking Math Class with Python"""

import time
from math import sqrt
start_time = time.perf_counter_ns()

def factors(n):
    """Returns a list of the factors of n"""
    output = []
    for i in range(1,n+1):
        if n % i == 0:
            output.append(i)
            output.append(-i)
    return output 

def factor_polynomial(a,b,c):
    """Factors the polynomial a*x**2 + b*x + c if possible
    prints out (dx + e)(fx + g)"""
    afacts = factors(abs(a))
    cfacts = factors(abs(c))
    #choose a factor of a (d), then f is a/d and so on
    for d in afacts:
        for g in cfacts:
            f = a/d
            e = c/g
            if e*f + d*g == b:
                print("{}*x**2 + {}*x + {} = ({}x + {})({}x + {})".format(a,b,c,d,int(e),int(f),g))
                return
    #return False

def is_discriminant_square(a,b,c):
    """a,b,c, are coeffs of a*x**2 + b*x + c. Returns True if
    discriminant is a perfect square."""
    disc = b**2 - 4*a*c
    if disc < 0:
        return False
    return sqrt(disc) == int(sqrt(disc))

##print(is_discriminant_square(4,20,25)) #4*x**2 + 20*x + 25 = (2x + 5)**2
##print(is_discriminant_square(1,5,6)) #not a perfect square, but factorable
##print(is_discriminant_square(4,-11,5)) #not factorable

for i in range(2):
    start_time = time.perf_counter_ns()
    n = 0
    factorable = 0

    NUMS = list(range(-10,0)) + list(range(1,11))

    for a in NUMS:
        for b in NUMS:
            for c in NUMS:
                factor_polynomial(a,b,c)

    '''for a in NUMS:
        for b in NUMS:
            for c in NUMS:
                n += 1
                if i == 0:
                    if factor_polynomial(a,b,c):
                        factorable += 1
                else:
                    if is_discriminant_square(a,b,c):
                        factorable += 1
    print()
    if i == 0:
        print("Factoring function:")
    else:
        print("Checking Discriminant:")
        
    print("Number of trinomials:",n)
    print("Factorable: ",factorable)
    print("Percentage:",factorable/n*100)'''

    end = time.perf_counter_ns()
    
    print("Time (secs):",round((end-start_time)/1000000000,2))

    
#Factor 6*x**2 + x - 12. Spoiler alert: it's (2*x + 3)*(3*x - 4)
#factor_polynomial(6,1,-12)'''
