# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:39:15 2020

@author: Mukund Rastogi
"""

li=list(map(str,input("Enter list elements:").split()))
tup=tuple(li)
element=input("count occurance of ")
print("ocurrence of element is:",tup.count(element))
