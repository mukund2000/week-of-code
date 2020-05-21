# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:39:21 2020

@author: Mukund Rastogi
"""

s=input("Enter a string")
result=[]
def permute(data, i, length):  
    if i == length:  
        result.append(''.join(data) ) 
    else:  
        for j in range(i, length):  
            data[i], data[j] = data[j], data[i]  
            permute(data, i + 1, length)  
            data[i], data[j] = data[j], data[i]   

permute(list(s),0,len(s))

print(str(result))
