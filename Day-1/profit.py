# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:53:03 2020

@author: Mukund Rastogi
"""

cp=float(input("Enter cost price"))
sp=float(input("Enter selling price"))
profit=((sp-cp)/cp)*100
print("Profit in percent:",profit)
increment=1.05*(sp-cp)+cp
print("to increase the profit by 5% the selling price is:",increment)