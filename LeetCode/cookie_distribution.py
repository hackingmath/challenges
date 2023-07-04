from itertools import combinations
import random, math

def distributeCookies(cookies, k):
    lowest = math.inf
    for j in range(1000):
        bags = {i: list() for i in range(k)}
        # bag = 0
        unfairness = 0
        bag_seq = [random.randint(0,k-1) for i in range(len(cookies))]
        print("bag_seq:",bag_seq)
        for i,v in enumerate(bag_seq):
            bags[v].append(cookies[i])
        # bag+=1
        max_bag = 0
        print(bags)
        for b in bags:
            if bags[b]:
                if sum(bags[b]) > max_bag:
                    max_bag = sum(bags[b])
        unfairness = max_bag
        print("unfairness:",unfairness)
        if unfairness < lowest:
            lowest = unfairness
        print("lowest:",lowest)

#print(distributeCookies([8,15,10,20,8],2))
print(distributeCookies([6,1,3,2,2,4,1,2],3))
