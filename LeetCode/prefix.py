# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix

strs = ["ab","a"]
def pref():
    output = ""
    for i in range(len(strs[0])+1):
        output = strs[0][:i]
        for s in strs:
            #output = strs[0][:i]
            print(i,s[:i+1])
            if s[:i+1] != strs[0][:i+1]:
                return output
    return output
print("pref:",pref())