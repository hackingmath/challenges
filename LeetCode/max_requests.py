import itertools


def maximum_requestsOLD(n,requests,testing = False):
    output = 0
    #okbldgs = list() #
    from_to_dict = {i: [0, 0] for i in range(n)}
    for req in requests:
        fr, t = req
        from_to_dict[fr][0] += 1
        from_to_dict[t][1] += 1
    if testing:
        print("fr-to:",from_to_dict)
    # for bldg in from_to_dict:
    #     if from_to_dict[bldg][0] == from_to_dict[bldg][1]:
    #         okbldgs.append(bldg)
    # if testing:
    #     print("ok:",okbldgs)
    for r in requests:
        if testing:
            print("r:",r)
        if r[0] == r[1]:
            output += 1
            if testing:
                print("[x,x]",output)
            #requests.remove(r)
        # if all([n in okbldgs for n in r]):
        #     output += 1

        elif r[::-1] in requests:
            output += 2
            requests.remove(r)
            requests.remove(r[::-1])
    # for b in from_to_dict:
    #     output += min(from_to_dict[b])
    return output

def maximum_requests2(n,requests,testing=False):
    output = 0
    requests2 = requests[::]
    if testing:
        print('2:',requests2)
    from_to_dict = {i: [0, 0] for i in range(n)}

    for r in requests:
        if r not in requests2:
            continue
        if testing:
            print("r:", r)
        if r[0] == r[1]:
            output += 1
            if testing:
                print("output:", output)
            requests2.remove(r)
            if testing:
                print(requests2)
        # if all([n in okbldgs for n in r]):
        #     output += 1

        elif r[::-1] in requests2:
            output += 2
            if testing:
                print("-1,before:",requests2)
            requests2.remove(r)
            requests2.remove(r[::-1])
            if testing:
                print("-1,after:",requests2)
            if testing:
                print("output:", output)
    for req in requests2:
        fr, t = req
        from_to_dict[fr][0] += 1
        from_to_dict[t][1] += 1
    #create copy
    from_to_dict2 = from_to_dict.copy()
    if testing:
        print("fr-to:",from_to_dict)
    for b in from_to_dict:

        if testing:
            print("b:",from_to_dict[b])
        if 0 in from_to_dict[b]:
            del from_to_dict2[b]
            if testing:
                print("fr-to2:", from_to_dict2)
            if len(from_to_dict2) == 1:
                return output
            continue


        #else:
    for b in from_to_dict2:
        output += min(from_to_dict2[b])
        if testing:
            print("min output:", output)
    return output

def maximum_requests(n,requests,testing=False):
    for k in range(len(requests),0,-1):
        for c in itertools.combinations(range(len(requests)),k):
            degree = [0]*n
            for i in c:
                degree[requests[i][0]] -= 1
                degree[requests[i][1]] += 1
            if not any(degree):
                return k
    return 0

print(maximum_requests(5,[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]),"expected 5")
print(maximum_requests(4,[[0,3],[3,1],[1,2],[2,0]],False),"expected 4")
print(maximum_requests(3,[[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]],False),"expected 4")
print(maximum_requests(2,[[1,1],[1,0],[0,1],[0,0],[0,0],[0,1],[0,1],[1,0],[1,0],[1,1],[0,0],[1,0]],False),"expected 11")
print(maximum_requests(3,[[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]],False),"expected 5")#5
print(maximum_requests(3,[[1,2],[0,0],[0,2],[0,1],[0,0],[0,2],[1,0],[0,1],[2,0]],True),"expected 7")