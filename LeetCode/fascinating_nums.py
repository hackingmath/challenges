def isFascinating(n):
    strn = str(n) + str(2 * n) + str(3 * n)
    print(strn)
    return all([strn.count(c) == 1 for c in '123456789'])

print(isFascinating(783))