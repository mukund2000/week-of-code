# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:57:57 2020

@author: Mukund Rastogi
"""

li=list(map(str,input().split()))

def duplicate(li):
    dup=[]
    for i in li:
        if i not in dup:
            dup.append(i)
    return dup

print(duplicate(li))