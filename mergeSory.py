'''
Author: Sabrina Wasserman
Date: December 1, 2015
Title: mergeSort
Purpose: to run merge sort on these algorithms
'''

num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array



def mergeSort(list):
    if len(list)<=1: return list

    #Dividing up the List
    middleOfList = len(list)/2
    listFirstHalf = list[: middleOfList]
    listSecondHalf = list[middleOfList :]

    #Running merge sort recursively to shorten the list
    leftSideArray = mergeSort(listFirstHalf)
    rightSideArray = mergeSort(listSecondHalf)

    #Merging the values
    return merge(leftSideArray, rightSideArray)

def merge(leftSide, rightSide):
    if len(leftSide) == 0: return rightSide
    elif len(rightSide) == 0: return leftSide

    if leftSide[0] <= rightSide[0]:
        return [leftSide[0]] + merge(leftSide[1:], rightSide)

    else:
        return [rightSide[0]] + merge(leftSide, rightSide[1:])

print 'Your sorted list (using Merge Sort): ', mergeSort(num_array)
