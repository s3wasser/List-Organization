'''
Created on Nov 26, 2015

@author: Sabrina
'''

num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array


def shell(list):
    gap = len(list)/2
    while gap>0:
        for i in range(0, gap):
            #Run insertion sort
            insertGap(gap, list, i)
        gap= gap/2
    return list

def insertGap(theGap, list, start):
    #Running for the length of the list
    for x in range(start+theGap, len(list), theGap):
        j = x
        
        #moves the value forward
        while j>start and list[j]<list[j-theGap]: 
            list[j],list[j-theGap] = list[j-theGap], list[j]
            j = j-theGap

print 'Your sorted list (using shell sort): ', shell(num_array)