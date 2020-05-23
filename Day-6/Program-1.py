# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:25:35 2020

@author: Mukund Rastogi
"""

def longestPalllindrome(s):
    n=len(s)
    li=[[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        li[i][i]=1
        for cl in range( 2, n+1): 
            for i in range(n - cl + 1): 
                j = i + cl - 1
                if (s[i] == s[j] and cl == 2): 
                    li[i][j] = 2
                elif (s[i] == s[j]): 
                    li[i][j] = li[i + 1][j - 1] + 2
                else: 
                    li[i][j] = max(li[i][j - 1],li[i + 1][j])
    return li[0][n-1]

def numberofDeletion(s):
    n=len(s)
    l=longestPalllindrome(s)
    return (n-l)

s=input("Enter the string")
print("Number of deletion to make pallindrom :",numberofDeletion(s))