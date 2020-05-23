# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:03:58 2020

@author: Mukund Rastogi
"""
def knapSack(cap,li):
    if cap==0 or len(li)==0:
        return 0
    if len(li)==1:
        if li[0][0]>cap:
            return 0
        return li[0][1]
    if li[0][0]>cap:
        return knapSack(cap,li[1:])
    return max(li[0][1]+knapSack(cap-li[0][0],li[1:]),knapSack(cap,li[1:]))

sz=int(input("Enter the size of list"))
Li=[]
for i in range(sz):
    wt=int(input("Enter the weight: "))
    val=int(input("Enter the value: "))
    Li.append((wt,val))
capacity=int(input("Enter the capacity: "))
print("Maximum value: ",knapSack(capacity,Li))
