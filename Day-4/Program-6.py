# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:55:32 2020

@author: Mukund Rastogi
"""

sd=int(input("Enter the size of dictionary"))
dictionary=[]
for i in range(sd):
    dictionary.append(input("Enter words in list: "))

ar=[]
res=[]
sa=int(input("Enter the size of array"))
for i in range(sa):
    ar.append(input("Enter characters in array: "))
for word in dictionary:
    if set(word).issubset(set(ar)):
        res.append(word)

print(",".join(res)+".")
