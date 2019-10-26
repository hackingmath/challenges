"""Quadratic File Exploration
Euler-like challenge to take a file of quadratic
equations, solve them and provide the sum of their solutions
October 26, 2019"""

import random
from math import sqrt

def quad(a,b,c):
    """Solves quadratic equations and returns the sum
    of the solutions."""
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1,x2
    
def solve():
    """Reads file of quadratic coefficients,
    returns sum of all roots"""
    running_sum = 0
    with open("quadtratics.txt",'r') as f:
        for i in range(100):
            g = f.readline().split()
            a,b,c = int(g[0]),int(g[1]),int(g[2])
            s1,s2 = quad(a,b,c)
            running_sum += (s1+s2)
            print(s1,s2,running_sum)
    print(running_sum)

solve()

    
def generate(num):
    """Generates a given number of quadratic
    expressions ax**2 + bx + c denoted by 3
    numbers separated by spaces. Saves running
    sum."""
    coeffs = list(range(-10,0)) + list(range(1,11))
    
    running_sum = 0
    total = 0

    with open("quadtratics.txt",'w') as f:
        while total < num:
            try:
                #assign random integers to a,b,c
                a = random.choice(coeffs)
                b = random.choice(coeffs)
                c = random.choice(coeffs)
                #make sure solution is real
                running_sum += quad(a,b,c)
                #if no exception:
                f.write(str(a)+' '+str(b)+' '+str(c)+'\n')
                total += 1
            except ValueError:
                continue

    print(running_sum) #-33.278968253968245
              
#generate(100)
    
