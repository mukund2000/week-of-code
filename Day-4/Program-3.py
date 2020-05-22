# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:35:09 2020

@author: Mukund Rastogi
"""

sz=int(input("Enter the size of dictionary: "))
d={}
for i in range(sz):
    key=input("Enter the key elelment:")
    value=int(input("Enter the value in dictionary: "))
    d[key]=value
    
print("The 2nd maximum number is: ",list(sorted(d.values()))[-2])

