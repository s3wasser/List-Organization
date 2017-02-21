'''
Created on Nov 25, 2015

@author: Sabrina
'''

num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array


def bubbleSortList(userList):
    for i in range (1, len(userList)):
            for x in range (0, len(userList)-1):
             if userList[x] > userList[x+1]:
                 userList[x], userList[x+1] = userList[x+1], userList[x]

    return userList

print 'Your sorted list (using bubble sort): ', bubbleSortList(num_array)
