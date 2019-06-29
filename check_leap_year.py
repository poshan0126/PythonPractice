# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:21:01 2019

@author: Poshan Pandey
"""

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))