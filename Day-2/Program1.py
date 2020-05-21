# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:36:50 2020

@author: Mukund Rastogi
"""

def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False

def isArmstrong(n):
    temp=n
    s=0
    while(temp):
        rem=temp%10
        s=s+rem**3
        temp=temp//10
    if n==s:
        return True
    else:
        return False
    
def isPallindrome(n):
    temp=n
    rev=0
    while(temp>0):
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if rev==n:
        return True
    else:
        return False

def even(n):
    if(n%2==0):
        return True
    else:
        return False
def odd(n):
    if(n%2!=0):
        return True
    else:
        return False
n=int(input("Enter number"))
if(isPrime(n)):
    print("This is prime no.\n")
if(isArmstrong(n)):
    print("This is armstrong no.\n")
if(isPallindrome(n)):
    print("This is pallindrome no.\n")
if(even(n)):
    print("This is even no.\n")
if(odd(n)):
    print("This is odd no.\n")
