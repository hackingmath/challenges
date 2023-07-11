def canConstruct(ransomNote,magazine):
    noteset = set(ransomNote)
    for letter in noteset:
        if magazine.count(letter) < ransomNote.count(letter):
            return False
    return True

tests = [['a','b'],['aa','ab'],['aa','aab']]
for t in tests:
    print(canConstruct(t[0],t[1]))