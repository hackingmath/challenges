def sum_of_n(n, a1, an):
    return n / 2 * (a1 + an)


def missingNumber(nums):
    #sorted_nums = sorted(nums)
    a1,an = min(nums),max(nums)
    n = an-a1+1
    return sum_of_n(n,a1,an)-sum(nums)

def brute_force(nums):
    a,z = min(nums),max(nums)
    for n in range(a+1,z):
        if n not in nums:
            print("Missing Number:",n)
            return

#print(sum_of_n(100,1,100))
#print(missingNumber([9,6,4,2,3,5,7,0,1]))
brute_force()