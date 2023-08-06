def wordBreak2(s,wordDict):
    def construct(current, wordDict, memo={}):
        if current in memo:
            return memo[current]

        if not current:
            return True

        for word in wordDict:
            if current.startswith(word):
                new_current = current[len(word):]
                if construct(new_current, wordDict, memo):
                    memo[current] = True
                    return True

        memo[current] = False
        return False

    return construct(s, wordDict)

def wordBreak(s,wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[-1]

print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak("bb",["a","b","bbb","bbbb"]))
print(wordBreak('cars',["car","ca","rs"]))
print(wordBreak("aaaaaaaa",["aaaa","aaa","aa"]))
print(wordBreak("goalspecial",["go","goal","goals","special"]))