'''CodeWars challenge
https://www.codewars.com/kata/59d902f627ee004281000160
October 30, 2018'''

def str_sort(arr):
    '''Sorts a list of integers to return
    the highest integer'''
    #if the array has 10 items, sort 9 times
    for j in range(len(arr)-1):
        #compare every item with the next one
        for i in range(len(arr)-1):
            #the two strings in order in the list
            a,b = arr[i], arr[i+1]
            #if ab is less than ba, switch them
            if int(str(a)+str(b)) < int(str(b)+str(a)):
                arr[i],arr[i+1] = arr[i+1],arr[i]
            print(arr)
    return arr

def largest_arrangement(numbers):
    numstrings = [str(i) for i in numbers]
    numstrings = sorted(numstrings)
    numstrings = numstrings[::-1]
    output = ''
    for i in numstrings:
        output += i
    #print(numstrings)
    return int(output)

print(str_sort([6, 73, 79, 356, 7]))
