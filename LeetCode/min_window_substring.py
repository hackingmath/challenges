#https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def contains_all(self,s,letters):

        for letter in letters:
            if letter not in s:
                return False
            if s.count(letter) < letters.count(letter):
                return False
        return True

    def minWindow(self, s: str, t: str,testing:bool) -> str:
        tletters = {letter:t.count(letter)for letter in t}
        for i in range(len(t),len(s)+1):
            for j in range(len(s)-len(t)+1):
                substr = s[j:j+i]
                subletters = {letter: substr.count(letter) for letter in t}
                if testing:
                    print("i,j,substr:",i,j,substr)
                if tletters == subletters:
                    return substr
                # if s.count(letter) < t.count(letter):
                #     return ""
                # if self.contains_all(substr,t):
                #     return substr
        return ""

a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC",False))
#print(a.minWindow("aabb","aba",True))
#print(a.minWindow("a", "a",True))

#print("len(t):",len(t))

# c = {'x':3,'y':4}
# d = {'y':4,'x':3}
#
# print("c==d?",c==d)