# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:36:07 2020

@author: Mukund Rastogi
"""

MAX = 100005
fibonacci = set() 
   
def createHash(): 
    global fibonacci 
    prev , curr = 0, 1
    fibonacci.add(prev) 
    fibonacci.add(curr) 
 
    while (curr <= MAX): 
        temp = curr + prev 
        if temp <= MAX: 
            fibonacci.add(temp) 
        prev = curr 
        curr = temp 
   
def checkArray(arr, n): 
    sum = 0
    for i in range( n ): 
        if (arr[i] in fibonacci): 
            sum += arr[i] 
    if (sum in fibonacci): 
        return True
    return False

n=int(input("Enter the size of array:"))
arr=list(map(int,input("Enter the elements: ").split()))
createHash()
if(checkArray(arr,n)):
    print("YES")
else:
    print("NO")
   