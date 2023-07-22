def find_n(arr,tot):
    # for w in range(1,1000000000):
    #     running_sum = 0
    #     if sum([(i+2*w)**2 for i in arr]) == tot:
    #         return w
    c = sum([i**2 for i in arr]) - tot
    b = sum([4*i for i in arr])
    a = 4*len(arr)
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    return int(x1)

with open("cardboard.txt",'r') as f:
    t = int(f.readline())
    for i in range(t):
        n,tot = [int(x) for x in f.readline().split()]
        ps = [int(x) for x in f.readline().split()]
        print(find_n(ps,tot))
