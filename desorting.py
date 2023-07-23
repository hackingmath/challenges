with open('desorting.txt','r') as f:
    T = int(f.readline())
    for _ in range(T):
        n = int(f.readline())
        nums = [int(x) for x in f.readline().split()]
        if nums != sorted(nums):
            print(0)
            break
        diffs = [nums[i] - nums[i-1] for i in range(1,len(nums))]
        maxdif = min(diffs)
        print(maxdif//2+1)

