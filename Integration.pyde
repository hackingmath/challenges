#grid.pyde

import math

#set the range of x-values
xmin=-10
xmax=10

#range of y-values
ymin = -5
ymax = 5

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl= width / rangex
    yscl= -height / rangey

def draw():
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    
    noFill()
    strokeWeight(1) #thicker line
    stroke(0) #black
    
    strokeWeight(2) #thicker line
    stroke(255,0,0) #red

    #line(0,0,3*xscl,6*yscl)
    #fill(255,0,0)
    #ellipse(3*xscl,6*yscl,10,10)
    graphFunction()
    drawIntegral(f,0,PI/2,100)

    
    
def f(x):
    #return 6*x**3 + 31*x**2 + 3*x - 10
    return (math.asin(math.sin(x)/math.sqrt(2))*math.sin(x))/ \
    (math.sqrt(4-2*(math.sin(x)**2))) 

def graphFunction():
    x = xmin
    while x <= xmax:
        fill(0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
    
def grid(xscl, yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0, xmax*xscl,0)
    
def drawIntegral(f,a,b,number_of_rects):
    the_range = b - a
    interval = the_range / float(number_of_rects)
    the_sum = 0
    x = a
    for i in range(number_of_rects):
        the_sum += f(x) * interval
        fill(255,0,0,50)
        rect(x*xscl, 0,interval*xscl,f(x)*yscl)
        x += interval
    println(the_sum)
