# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:26:30 2020

@author: Mukund Rastogi
"""

n=int(input("Enter number"))
for i in range(n):
    print((str(n-i)+"*")*(n-i-1)+str(n-i))
for i in range(2,n+1):
    print((str(i)+"*")*(i-1)+str(i))