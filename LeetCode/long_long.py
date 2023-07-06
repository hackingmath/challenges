def neg_in_list(arr):
    return any([n<0 for n in arr])

def reverse_nums(nums):
    start = 0
    end = len(nums)-1
    times = 0
    while any([n < 0 for n in nums]):
        while end > start and nums[start] >= 0:
            start += 1
        while nums[end] >= 0:
            end -=1
        negative_part = [-1*n for n in nums[start:end+1]]
        newnums = nums[:start]+negative_part+nums[end+1:]
        times += 1
        nums = newnums[::]
    return sum(nums),times

def num_switches(nums):
    total = 0
    first = True
    neg = False
    for i,v in enumerate(nums):
        if v == 0: continue
        if v < 0:
            if not neg:
                neg = True
                if first:
                    first = False
                    continue
                total += 1
                #print("neg switch")
        else: #positive
            if neg:
                neg = False
                total += 1
                #print("pos switch")
    return sum([abs(n) for n in nums]),int(total/2) + 1

#print(num_switches([-3,-2]))


num_tests = int(input())
for i in range(num_tests):
    num_items = input()
    nums = [int(x) for x in input().split(' ')]
    if not any([n<0 for n in nums]):
        print(sum([abs(n) for n in nums]),0)
    else:
        ans1,ans2 = num_switches(nums)
        print(ans1,ans2)

