def buddy_strings(s,goal,testing = True):
    if len(s) != len(goal):
        return False
    s,goal = list(s),list(goal)
    news = s[::]
    for i in range(len(s)):
        for j in range(len(s)):
            news = s[::]
            if i == j:
                continue
            news[i],news[j] = s[j],s[i]
            print(i,j,news)
            if news == goal:
                if testing:
                    print(i,j,news,s,goal)
                return True
    return False

print(buddy_strings("aaaaaaabc","aaaaaaacb",True))