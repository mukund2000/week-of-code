# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:32:04 2020

@author: Mukund Rastogi
"""

def replacedigits(num):
    return int(str(num).replace('0','5'))

number=int(input("Enter number :"))
print("Replacing 0 with 5 after number is: ",replacedigits(number))
