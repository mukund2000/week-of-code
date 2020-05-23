# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:17:48 2020

@author: Mukund Rastogi
"""

def EvenOdd(li):
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(odd,reverse=True)+sorted(even)


sz=int(input("enter the size of list"))
li=list(map(int,input("Enter the list element: ").split()))
print("The customized array is: ",EvenOdd(li))