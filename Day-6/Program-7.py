# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:54:03 2020

@author: Mukund Rastogi
"""

def Ackermann(m, n, s ="% s"): 
    print(s % ("A(% d, % d)" % (m, n))) 
    if m == 0: 
        return n + 1
    if n == 0: 
        return Ackermann(m - 1, 1, s) 
    n2 = Ackermann(m, n - 1, s % ("A(% d, %% s)" % (m - 1))) 
    return Ackermann(m - 1, n2, s) 

n,m=map(int,input("Enter the value of n and m:").split())
print(Ackermann(m, n)) 