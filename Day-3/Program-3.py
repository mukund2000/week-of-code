# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:53:04 2020

@author: Mukund Rastogi
"""

s=input("Enter string")

def duplicate(s):
    dup="";
    for x in s:
        if x not in dup:
            dup+=x
    return dup
print(duplicate(s))
    