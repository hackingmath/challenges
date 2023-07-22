def max_streak(arr,d):
    output,streak = 0,0
    for i in range(1,len(arr)):

        #print(arr[i])
        if (arr[i] - arr[i-1]) <= d:
            streak += 1
            output = max(output,streak)
            #print("streak,output:",streak,output)
        else:
            streak = 0
    return len(arr)-output-1

with open("children.txt",'r') as f:
    t = int(f.readline())
    for i in range(t):
        n=int(f.readline())
        frog_dict = {j:0 for j in range(1,n+1)}
        jumps = [int(x) for x in f.readline().split()]
        for jump in jumps:
            x = 1
            while x*jump <= n:
                frog_dict[x*jump] += 1
                x += 1
        print(frog_dict)
        print(max(frog_dict.values()))