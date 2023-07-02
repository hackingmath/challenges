import time
from math import sqrt

start_time = time.time()

def alternating(nums,threshold):
    even = False
    evens = list()
    for i in nums:
        if i % 2 == 0:
            evens.append(0)
        else:
            evens.append(1)
    longest = 0
    length = 0
    even = False
    for i in range(0,len(evens)):
        if evens[i] == 1 and not even:
            print("not even",nums[i])
            print("longest:",longest)
            continue
        if evens[i] == 0 and not even and nums[i] <= threshold:
            even = True
            length = 1
            print("First even:",nums[i])
            print("length:", length)
        elif even and (evens[i] == 1 - evens[i-1]) and nums[i] <= threshold:
            length += 1
            print("even and alternating",nums[i])
            print("length:", length)
        elif even and (evens[i]==0) and nums[i] <= threshold:
            length = 1
            print("new even:",nums[i])
        else:
            even = False
            length = 0
            print("Else length:", length)

        if length > longest:
            longest = length
            print("longest:", longest)

        # if v == 0 and even == False and nums[i] <= threshold:
        #     even = True
        #     length += 1
        # elif v == 1:
        #     if even == False:
        #         length = 0
        #         continue
        #     else:
        #         if length == 0:
        #             continue
        #         even = False
        #         if nums[i] <= threshold:
        #             length += 1

    return longest

#n= [2,3,4,5]
#print(alternating([3,2,5,4],5))#expecting 3
print(alternating([4,10,3],10))#expecting 2
#n = [2,10,5]
#n = [2,2]

#print(alternating(n,18))

def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#primes = [i for i in range(2,10**6) if is_prime(i)]
#print("primes:",primes[:10])

def findPrimePairs(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    output = []
    for i in primes:
        print(i)
        if i > n/2:
            return output
        if n-i in primes:
            output.append([i,n-i])
    return output

#print(findPrimePairs(100))

print("Time:",round(time.time()-start_time,1))