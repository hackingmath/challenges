def fibo(n,k,testing=False):
    ways = 0
    #j = 0
    for j in range(n):#while True:

        nums = [n]
        step = n//k+j
        for i in range(k-1):
            if testing:
                print("i,j:", i,j)
            if i == 0:
                nums.append(nums[-1]-step)
            else:
                nums.append(nums[-2]-nums[-1])
            if testing:
                print(nums)
            if nums[-1] > nums[-2]:
                j += 1
                break
            if len(nums) == k:
                ways += 1
                break
            if i < k-1 and nums[-1] < 0:
                j += 1
                if testing:
                    print("break")
                break
            if i == k-1:
                ways += 1
                j += 1
        if n//k + j > n//2:
            return ways
    return ways

with open("fibonaccharsis.txt",'r') as f:
    T = int(f.readline())
    for i in range(T):
        n,k = [int(x) for x in f.readline().split()]
        print(fibo(n,k))
