# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:36:16 2020

@author: Mukund Rastogi
"""
import sys
def checkIfSortRotated(arr, n): 
    minEle = sys.maxsize 
    maxEle = -sys.maxsize - 1
    minIndex = -1
    for i in range(n): 
        if arr[i]< minEle: 
            minEle = arr[i] 
            minIndex = i 
    flag1 = 1
    
    for i in range(1, minIndex): 
        if arr[i] < arr[i - 1]: 
            flag1 = 0
            break
    flag2 = 2
  
    for i in range(minIndex + 1, n) : 
        if arr[i] < arr[i - 1]: 
            flag2 = 0
            break
        
    if (flag1 and flag2 and 
        arr[n - 1] < arr[minIndex - 1]): 
        print("YES") 
    else: 
        print("NO") 
  
n=int(input("Enter the size of array:"))
arr=list(map(int,input("Enter the elements: ").split()))
checkIfSortRotated(arr,n)