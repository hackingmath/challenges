'''divisibility brainteaser
30 students say one thing about a number
It's divisible by 2, by 3, by 4, all the way up
to 31. The teacher says 2 students, who spoke
*consecutively* spoke wrongly. Which 2?
November 5, 2018'''

from math import sqrt

def div_num(n):
    '''Tests whether a number is divisible by
    all the numbers up to 31 except 2'''
    exceptions = []
    for i in range(2,32):
        if n % i != 0:
            exceptions.append(i)
        if len(exceptions) > 2:
            return False
    if len(exceptions) == 2 and (exceptions[1] - exceptions[0] == 1):
        print(n,exceptions)
        return True
    print(exceptions)


'''
The smallest number divisible by all of them is
2*3*4*5*7*9*11*13*16*17*19*23*25*29*31
You can't take out any of the other consecutive factors
without screwing up the later ones, so the last pair
16*17
is the pair to take out. The number will be divisible
by all the other numbers up to 31. Look!

>>> a = 2*3*4*5*7*9*11*13*19*23*25*29*31
>>> a
10617908301000
>>> div_num(a)
10617908301000 [16, 17]
True
'''

def divis(n):
    '''prints out all the numbers n is divisible by'''
    for i in range(2,n+1):
        if n % i == 0:
            print(i,end = ", ")

#let's make a function for the smallest number divisible by 2 through n:

def isPrime(n):
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0: return False
    return True

def factorNum(n):
    '''Returns a list of prime factors of n

    >>> factorNum(60)
    [2, 2, 3, 5]
    '''
    output = []
    #list of primes lower than sqrt(n)
    primes = [i for i in range(2,int(sqrt(n))+1) if isPrime(i)]
    if isPrime(n): return [n]
    while not isPrime(n):
        for p in primes:
            if n % p == 0:
                output.append(p)
                n /= p # replace n by n divided by p
    output.append(int(n))
    output = sorted(output)
    return output
    

def smallestDivisible(n):
    '''Returns smallest number divisible by
    all the integers from 2 through n'''
    factors = []
    for i in range(2,n+1):
        if isPrime(i):
            factors.append(i)
        else:
            factors2 = factorNum(i)
            for f in factors:
                '''if factors.count(f) < factors2.count(f):
                    factors.append(i)'''
                if i % f == 0:
                    i /= f
            factors.append(int(i))
                    #break
        #print("factors:",factors)
    output = 1
    for f in factors:
        output *= f
    return output

    
