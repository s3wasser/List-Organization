'''
Author: Sabrina Wasserman
Date: November 19, 2015
Title: insertionSort.py
Purpose: to use loops to create an insertion sort
'''

num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array


def insertSort(userList):
    #Running for the length of the list
    for i in range(1, len(userList)):
        j = i
    
        #moves the value forward
        while j>0 and userList[j]<userList[j-1]: 
            userList[j],userList[j-1] = userList[j-1], userList[j]
            j = j-1
    return userList   

print 'Your sorted list (using insertion sorted): ', insertSort(num_array)