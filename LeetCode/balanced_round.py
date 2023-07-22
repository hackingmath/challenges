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

#with open("balanced_round.txt",'r') as f:
t = int(input())
for i in range(t):
    n,sep = [int(x) for x in input().split()]
    output = 0
    diffs = sorted([int(x) for x in input().split()])
    #print(n,sep,diffs)
    #print(output)
    print(max_streak(diffs,sep))