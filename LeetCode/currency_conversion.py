#From video
#July 1, 2023

import time
from collections import deque

time1 = time.time()

def convert_currency(arr,start,end,testing=False):
    """Array of from->to,rate lists and a desired start
    and end currency."""
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

def convert_curency(convertion_list, starting, ending):
    if starting == ending:
        return 1.
    for conversion in convertion_list:
        if starting in conversion:
            if ending in conversion:
                if starting == conversion[0]:
                    return conversion[2]
                else:
                    return 1./conversion[2]
            if starting == conversion[0]:
                current_conversion = conversion[2]
                new_list = convertion_list
                new_list.remove(conversion)
                following_conversion = convert_curency(new_list,
                                                       conversion[1],
                                                       ending)
            else:
                current_conversion = 1./conversion[2]
                new_list = convertion_list
                new_list.remove(conversion)
                following_conversion = convert_curency(new_list,
                                                       conversion[0],
                                                       ending)
            if following_conversion:
                    return current_conversion*following_conversion
    return None

# print(convert_curency([["USD","JPY",110],
#                   ["USD","AUD",1.45],
#                   ["JPY","GBP",0.0070]],
#                  "GBP","AUD"))

#Answer check: 1.89
print("Time:",round(time.time() - time1,1))