# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:05:18 2020

@author: Mukund Rastogi
"""

n=int(input("enter number"))
for i in range(n):
    print(" "*i + "*" + " "*(n-i-1)*2 + "*")
for i in range(n):
    print(" "*(n-i-1) + "*" + " "*i*2 + "*")
    