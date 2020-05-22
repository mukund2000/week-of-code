# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:47:58 2020

@author: Mukund Rastogi
"""

n=int(input("Enter total no of votes"))
vote=[]
for i in range(n):
    vote.append(input("Enter the name of candiadate"))

candidate=[]
for name in vote:
    candidate.append((name,vote.count(name)))

candidate.sort(key=lambda x:x[0],reverse=True)
candidate.sort(key=lambda x:x[1])
print("The candidate who won the election is :",candidate[-1][0])
