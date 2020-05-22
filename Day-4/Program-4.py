# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:39:54 2020

@author: Mukund Rastogi
"""

sz=int(input("Enter the size of dictionary: "))
d={}
for i in range(sz):
    key=input("Enter the key elelment:")
    value=int(input("Enter the value in dictionary: "))
    d[key]=value

res={}
for key,value in d.items():
    if value not in res.values():
        res[key]=value
        
print("After removing duplicate from dictionary :",res)