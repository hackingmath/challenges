"""Factoring Polynomials
May 22, 2019
From Hacking Math Class with Python"""

import time
start_time = time.time()

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
                return True
    return False

n = 0
factorable = 0

NUMS = list(range(-20,0)) + list(range(1,21))

for a in NUMS:
    for b in NUMS:
        for c in NUMS:
            n += 1            
            if factor_polynomial(a,b,c):
                factorable += 1
            
print("Number of trinomials:",n)
print("Factorable: ",factorable)
print("Percentage:",factorable/n*100)

print("Time (secs):",round(time.time()-start_time,1))
#Factor 6*x**2 + x - 12. Spoiler alert: it's (2*x + 3)*(3*x - 4)
#factor_polynomial(6,1,-12)
