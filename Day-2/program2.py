# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:00:37 2020

@author: Mukund Rastogi
"""

def fibonacci(k):
    f=[]
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,k):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        
k=int(input("Enter no"))
fibonacci(k)