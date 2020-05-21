# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:05:05 2020

@author: Mukund Rastogi
"""

li1=list(map(str,input("enter list 1:").split()))
li2=list(map(str,input("enter list 2:").split()))
intersec=list(set(li1).intersection(set(li2)))
print("intersection of li1 and li2 is:",",".join(intersec))
