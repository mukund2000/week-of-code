# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:36:40 2020

@author: Mukund Rastogi
"""

def ReplaceWithGreatest(List):
    for i in range(len(List)-1):
        List[i]=max(List[i+1:])
    return List

n=int(input("Enter the size of list"))
List=list(map(int,input("Enter the elements in list: ").split()))
print("After sorting The list is: ",ReplaceWithGreatest(List))