from itertools import permutations

def wordBreak2(s,wordDict):
    n = [len(s) // len(word) for word in wordDict]
    for i, v in enumerate(wordDict):
        if v * n[i] == s:
            return True
    wordDict = sorted(wordDict,key=len)
    while len(s) > 0:
        if not any([word in s for word in wordDict]):
            return False
        for word in wordDict:
            print("word:",word)
            if word not in s:
                continue
            else:
                s = s.replace(word, '',1)
                print(s)
    return True

def wordBreak3(s,wordDict):
    n = [len(s) // len(word) for word in wordDict]
    for i,v in enumerate(wordDict):
        if v*n[i] == s:
            return True

def solve2(s,values, safe_up_to):
    """Finds a solution to a backtracking problem.

    values     -- a sequence of values to try, in order. For a map coloring
                  problem, this may be a list of colors, such as ['red',
                  'green', 'yellow', 'purple']
    safe_up_to -- a function with two arguments, solution and position, that
                  returns whether the values assigned to slots 0..pos in
                  the solution list, satisfy the problem constraints.
    size       -- the total number of “slots” you are trying to fill

    Return the solution as a list of values.
    """
    #values = sorted(values,key=len)
    def extend_solution(soln):
        for value in values:
            soln += value
            print("soln:",soln)
            if safe_up_to(s,soln):
                if soln == s or extend_solution(soln):
                    return True
            else:
                soln = soln[:-len(value)]

        return False

    return extend_solution('')

def wordBreak4(s,wordDict):
    for p in permutations(wordDict):
        print(p)
        if solve(s,p, check_no_conflicts, len(s)):
            return True
    return False

def check_no_conflicts(s,soln):
    sol = ''.join(soln)
    n = len(sol)
    #print('sol:',sol,s[:n],sol==s[:n])
    return sol == s[:n]

def solve(s,values, safe_up_to,testing=False):
    #values = sorted(values,key=len)

    def extend_solution(soln):
        if testing:
            print("extend:", soln)
        for i,value in enumerate(values):
            if testing:
                print("value:",value)
            soln.append(value)
            print("soln.append(value):",soln)
            if safe_up_to(s,soln):
                if ''.join(soln) == s or extend_solution(soln):
                    return True
            else:
                soln = soln[:-1]
                if testing:
                    print("soln[:-1]:",soln)
                if i == len(values)-1: #last word didn't work
                    idx = values.index(value)
                    soln[-1] = values[idx-1]


                    if testing:
                        print("soln[:-2]:", soln)

        return False

    return extend_solution([])

def wordBreak5(s,wordDict):
        #for p in permutations(wordDict):
    return solve(s,wordDict, check_no_conflicts,True)
                #return True
        #return False

print(wordBreak5("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak5("bb",["a","b","bbb","bbbb"]))
print(wordBreak5('cars',["car","ca","rs"]))
print(wordBreak5("aaaaaaaa",["aaaa","aaa","aa"]))
print(wordBreak5("goalspecial",["go","goal","goals","special"]))

from collections import deque

def wordBreak(s,wordDict):
    q = deque()
    for word in wordDict:
        q.append([word])
    while q:
        #print("q:",q)
        soln = q.popleft()
        #print("soln:",soln,type(soln))
        solnstr = ''.join(soln)
        n = len(solnstr)
        if n > len(s):
            continue
        #print("solnstr:",solnstr,len(solnstr))
        if solnstr == s: return True
        #print("so far:",solnstr, s[:n],solnstr == s[:n])
        if solnstr == s[:n]:

            for word in wordDict:
                a = soln[:]
                a.append(word)
                q.append(a)
    return False

# print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# print(wordBreak("bb",["a","b","bbb","bbbb"]))
# print(wordBreak('cars',["car","ca","rs"]))
# print(wordBreak("aaaaaaaa",["aaaa","aaa","aa"]))
# print(wordBreak("goalspecial",["go","goal","goals","special"]))

#print(solve("goalspecial",["goal","special","goals","go"],check_no_conflicts))