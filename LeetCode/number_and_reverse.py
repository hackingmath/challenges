def reversenum(num):
    numstr = str(num)
    revnum = int(numstr[::-1])
    return revnum

def sum_revnum(num):
    return num + reversenum(num)

def can_it_sum(num):
    for i in range(num,0,-1):
        if sum_revnum(i) == num:
            return True,i,reversenum(i)
    return False

for i in [443,63,181]:
    print(i,can_it_sum(i))