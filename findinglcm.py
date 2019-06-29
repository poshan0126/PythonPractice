# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:24:47 2019

@author: Poshan Pandey
"""

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


# uncomment the following lines to take input from the user
num1 = input("Enter first number: ")
num2 = (input("Enter second number: ")

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))