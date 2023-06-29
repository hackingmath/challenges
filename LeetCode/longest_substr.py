def length_longest(s,testing=False):
    longest = 0
    for i in range(len(s) - 1):
        for length in range(1, len(s) - i + 1):
            if testing:
                print(s[i:i + length])
            if len(list(s[i:i + length])) == len(set(s[i:i + length])):
                if longest < len(s[i:i + length]):
                    longest = len(s[i:i + length])
    return longest

#print(length_longest('au',True))


def lengthOfLongestSubstringOLD(s):
    if len(s) == 1: return 1
    longest = 0
    longstr = ''
    i = 0
    while i < len(s) - 1:
        # for i in range(len(s)-1):
        length = 1
        while length < len(s) - i + 1:
            # for length in range(1,len(s)-i+1):
            substr = s[i:i + length]
            for letter in substr:
                if substr.count(letter) > 1:

                    i = length + 1
                    length = i + 1
                    continue
            if len(list(s[i:i + length])) == len(set(s[i:i + length])):
                longstr = s[i:i + length]
                if longest < len(longstr):
                    longest = len(longstr)
            length += 1
        i += 1
    return longest,longstr

def lengthOfLongestSubstring(s):
    if len(s) == 1: return 1
    if len(s) == 0: return 0
    longest = 1
    longstr = s[0]
    streakon = True
    start,end = 0,1
    while start < len(s)-1:
        print("s[end],s[start:end]:",s[end], s[start:end])
        if s[end] in s[start:end]:
            start+=1
            end = start+ 1
            if streakon:
                streakon = False
                if streak > longest:
                    longest = streak
                    longstr = streakstr
        else:
            streakon = True
            streak = end-start+1
            streakstr = s[start:end+1] #+= s[end]
            print("streak,streakstr:", streak, streakstr)
            end += 1
            if end == len(s):
                print("end")
                if streak > longest:
                    longest = streak
                    longstr = streakstr
                return longest,longstr
        print("start,end:",start,end)
    return longest,longstr

#print(lengthOfLongestSubstring('dvdf'))

def easiest_longest_substring(s):
    n = len(s)
    charstr = ''
    maxLength = 0
    left = 0
    for right in range(n):

        if s[right] not in charstr:
            charstr += s[right]
            maxLength = max(maxLength,right - left +1)
        else:
            while s[right] in charstr:
                charstr = charstr[1:]
                left += 1
            charstr += s[right]

        print("charstr:", right, charstr)
    return maxLength

print(easiest_longest_substring('pkwekwe'))

