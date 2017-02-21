r'''
Author: Sabrina Wasserman
Date: November 24, 2015
Title: selectionSort
Purpose: to sort a list using selection sort
'''


num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array


'''
Title: sortList
Purpose: to sort the list using selection sort
@Param: int [] userList
@Reuturn: int [] updatedList
'''
def sortList(list):
    #Running through the list backwards
    for i in range (len(list) -1, 0, -1):

        #Resetting the max index to 0
        maxIndex = 0

        #Updating the max by iterating through the list
        for j in range (1, i+1):
            if list[j] > list[maxIndex]: maxIndex = j

        #Swapping values
        list[i], list[maxIndex] = list[maxIndex], list[i]

    return list

print 'Your sorted list (using selection sort): ', sortList(num_array)
