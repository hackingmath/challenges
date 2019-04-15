#calculus.py

import math

def f(x):
    '''Crazy CAS-stumping integral from
    The Computer as Crucible, p. 59'''
    return (math.asin(math.sin(x)/math.sqrt(2))*math.sin(x))/ \
    (math.sqrt(4-2*(math.sin(x)**2))) 

def integral(f,a,b,number_of_rects):
    the_range = b - a
    interval = the_range / number_of_rects
    total_area = 0
    x = a
    while x <= b:
        total_area += f(x)*interval
        x += interval
    return total_area


print(integral(f,0,math.pi/2,100) + \
      math.pi/8*math.sqrt(2)*math.log(2))

# Answer: 0.7742547356603636
