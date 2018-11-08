'''Best Divisor Challenge on Hackerrank'''

def factors(n):
    '''Returns a list of factors of n'''
    return [i for i in range(1,n+1) if n % i == 0]

def digits(n):
    if len(str(n)) == 1:
        return n
    strn = str(n)
    output = 0
    for digit in strn:
        output += int(digit)
    return output

def fave(n):
    facts = factors(n)
    values = {f:digits(f) for f in facts}
    ans = max(values, key=lambda key: values[key])
    print(ans)
    return(ans)

print(fave(98901))
