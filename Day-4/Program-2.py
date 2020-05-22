# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:15:22 2020

@author: Mukund Rastogi
"""

st=int(input("Enter the size of tuple in list"))
sl=int(input("Enter the size of List"))
List=[]
for i in range(sl):
    print("Enter the element in tuple",i+1)
    Tuple=[]
    for j in range(st):
        Tuple.append(int(input("Enter the element"+str(j+1)+"in Tuple:")))
    List.append(tuple(Tuple))
n=int(input("Enter the nth index about which sort the list"))
List.sort(key=lambda x:x[n])
print("Sorted list is:",List)
        