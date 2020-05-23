# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:44:43 2020

@author: Mukund Rastogi
"""

def missing(ar):
    m = max(ar) 
    if m < 1: 
        return 1 
    if len(ar) == 1: 
        return 2 if ar[0] == 1 else 1     
    l = [0] * m 
    for i in range(len(ar)): 
        if ar[i] > 0: 
            if l[ar[i] - 1] != 1: 
                l[ar[i] - 1] = 1 
    for i in range(len(l)): 
     if l[i] == 0:  
            return i + 1
    return i + 2

sz=int(input("Enter the size of the list:"))
li=list(map(int,input("Enter the element in the list: ").split()))
print("smallest missing number is :",missing(li))