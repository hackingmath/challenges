def gcf(a,b):
    factorsa = [i for i in range(1,a+1) if a % i == 0]
    factorsb = [j for j in range(1,b+1) if b % j == 0]
    for k in factorsb[::-1]:
        if k in factorsa:
            return k
    

def restaurant(l, b):
    #
    # Write your code here.
    #
    l,b = int(l),int(b)
    if l == b:
        return 1
    fac = gcf(l,b)
    return int((l*b)/(fac**2))

inp = '38 751 344 734 165 635 297 667 917 264 544 642 254 914 612 50 94 707 564 417 145 246'
inputList = inp.split(' ')
#print("inputList:",inputList)
newList = []
for i in range(0,len(inputList),2):
    newList.append([int(inputList[i]),int(inputList[i+1])])
print("newList:",newList)

for i in newList:
    print(restaurant(i[0],i[1]))
