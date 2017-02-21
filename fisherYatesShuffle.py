'''
Author: Sabrina Wasserman
Date: December 4, 2015
Title: fisherYatesShuffle
Purpose: to perform a fisher yates shuffle on the list
'''

num_array = list()
elements = raw_input("Please enter the number of elements in your array:")
print 'Enter each element of your array, followed by "enter"'
for i in range(int(elements)):
    n = raw_input('item ' + str(i+1) + ': ')
    num_array.append(int(n))
print 'Your list: ', num_array


#importing the random generator
import random
for i in range(len(num_array)-1, -1, -1):
    x = random.randrange(0, len(num_array))
    num_array[i], num_array[x] = num_array[x], num_array[i]
    
print 'Your shuffled list: ', num_array


