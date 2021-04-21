#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:40:12 2021

@author: Alaisha Naidu
Name: Daily Coding Problem 265
"""

#265

CodeLines = [10, 1000, 40, 200, 206, 600, 96, 10]

Bonus = []
for i in range(len(CodeLines)):
    j = i
    Bonus.append(i*0)     
    if CodeLines[i] == min(CodeLines):
        j = i
        Bonus[j] = 1

for i in range(0,len(CodeLines)-1):
    a =CodeLines[i]
    b =CodeLines[i+1]
    if  a < b:
        j = i
        Bonus[j+1] = Bonus[j] + 1 
    elif a > b:
        j = i
        Bonus[j+1] = Bonus[j] - 1
    elif a == b:
        j = i
        Bonus[j+1] = Bonus[j] 

for i in range(0,len(CodeLines)):
    if CodeLines[i] == min(CodeLines):
        j = i 
        Bonus[j] = 1 
    if CodeLines[i] == max(CodeLines):
        j = i
        Bonus[j]= max(Bonus)
 
print(Bonus)
        
        
    
        

