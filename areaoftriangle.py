
"""
Created on Sat Jun 29 20:07:44 2019

@author: Poshan Pandey
"""

a = input('Enter first side: ')
b = input('Enter second side: ')
c = input('Enter third side: ')

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)