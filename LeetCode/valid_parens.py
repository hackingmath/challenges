s="{[]}"


def isValid(s,testing=False):
    for i in range(5):
        s=s.replace("()", "").replace("{}", '').replace("[]", "")
        if testing:
            print(s)
    if len(s) == 0: return True
    for i, v in enumerate(s):
        if v == "(":
            if s[i + 1] != ")":
                return False
        elif v == "{":
            if s[i + 1] != "}":
                return False
        elif v == "[":
            if s[i + 1] != "]":
                return False
    return True

print(isValid(s,True))