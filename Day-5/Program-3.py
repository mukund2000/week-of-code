# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:50:39 2020

@author: Mukund Rastogi
"""

def Stolen(li):
    if len(li)==2:
        return max(li)
    if len(li)==1:
        return li[0]
    if len(li)==3:
        return max(li[1],li[0]+Stolen(li[2:]))
    return max(li[1]+Stolen(li[3:]),li[0]+Stolen(li[2:]))

n=int(input("Enter the size of list"))
li=list(map(int,input("Enter the list element :").split()))
print("MAximum stolen value from house is:",Stolen(li))