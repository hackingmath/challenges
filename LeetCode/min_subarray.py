import math
def minSubArrayLen(target,nums,testing=True):
    lowest = math.inf
    if target in nums:
        return 1
    for i in range(len(nums)):
        j = 1
        if testing:
            print("i,j:",i,j)
        while i+j < len(nums)+1 and sum(nums[i:(i + j + 1)]) <= target:
            if testing:
                print("subarray:",nums[i:i + j + 1],sum(nums[i:i + j + 1]))
            if sum(nums[i:i + j + 1]) >= target:
                if j+1 < lowest:
                    lowest = j+1
                    if testing:
                        print("lowest:",nums[i:i + j + 1],lowest)
                    continue
            j += 1
    if lowest == math.inf:
        return 0
    return lowest

print(minSubArrayLen(11,[1,2,3,4,5],True))

def tryagain(s,nums):
    ans = math.inf
    summ = 0
    j = 0

    for i, num in enumerate(nums):
      summ += num
      while summ >= s:
        ans = min(ans, i - j + 1)
        summ -= nums[j]
        j += 1

    return ans if ans != math.inf else 0

print(tryagain(11,[1,2,3,4,5]))
