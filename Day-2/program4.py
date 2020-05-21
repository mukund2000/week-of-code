# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:17:29 2020

@author: Mukund Rastogi
"""

n=int(input("Enter number"))
for i in range(n):
    print("* "*(n-i)+"  "*i*2+"* "*(n-i))
for i in range(2,n+1):
    print("* "*i+"  "*(n-i)*2+"* "*i)