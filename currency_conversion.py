#From video
#July 1, 2023

import time
from collections import deque

time1 = time.time()

def convert_currency(arr,start,end):
    """Array of from->to,rate lists and a desired start
    and end currency.
    """
    q = deque([(start,1)])

    while q:
        loc,num = q.popleft()
        if loc == end:
            return round(num,2)
        for a in arr:
            if loc in a:
                if loc == a[0]:
                    q.append((a[1],num*a[2]))
                elif loc == a[1]:
                    q.append((a[0],num/a[2]))


print(convert_currency([["USD","JPY",110],
                  ["USD","AUD",1.45],
                  ["JPY","GBP",0.0070]],
                 "GBP","AUD"))

#Answer check: 1.89
print("Time:",round(time.time() - time1,1))
