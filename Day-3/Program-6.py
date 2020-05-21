# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:08:24 2020

@author: Mukund Rastogi
"""
def Sum(Li,sz,sm):
    smli=[]
    if sz==1:
        for x in Li:
            smli.append(sm+x)
        return smli
    Li2=list(Li)
    for x in Li:
        Li2.remove(x)
        smli.extend(Sum(Li2,sz-1,sm+x))
    return smli

def summation(Li,sz):
    smli=list(Li)
    for i in range(2,sz+1):
        smli.extend(Sum(Li,i,0))
    num=1
    while True:
        if num not in smli:
            print("The least integer which is not present in the list and also can not represented as the summation of sub elements is:",num)
            break
        num+=1
        



n=int(input("Enter the size of list:"))
li=list(map(int,input("Enter the {} elements of list:".format(n)).split()))
summation(li,n)