def totalCost(costs, k, candidates,testing=False):
    total = 0
    for i in range(k):
        if len(costs) < candidates:
            mincost = min(costs)
            idx = costs.index(mincost)
            costs.remove(costs[idx])
            if testing:
                print(costs, mincost, idx, total)
            total += mincost
            return total
        else:
            mincost = min(costs)
            idx = costs.index(mincost)
            costs.remove(costs[idx])
            if testing:
                print(costs,mincost,idx,total)
            total += mincost
    return total

print(totalCost([1,2,4,1],3,3,True))