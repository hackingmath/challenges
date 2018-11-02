'''CodeWars challenge
https://www.codewars.com/kata/59d902f627ee004281000160
October 30, 2018'''

def str_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if int(str(arr[i])+str(arr[i+1])) < \
               int(str(arr[i+1])+str(arr[i])):
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
