#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:49:02 2021

@author: Alaisha Naidu
Name: Daily Coding Problem 266
"""

#266


from collections import Counter #Counter keeps a count of all the characters in a string (ie 4 a's, 6 b's, etc)

#Loop through a dictionary:
def DictionaryLoop(string1, dictionary):
    EqualLength = []
    for i in dictionary:
        if len(i) == len(string1)+1:
            EqualLength.append(i)
    print(EqualLength)
            
    
print(DictionaryLoop("silent", ["listens", "cat", "shreya"]))


def StepWord(string1, string2):
    str1 = list(string1)
    str2 = list(string2)
    diff = list((Counter(str1)-Counter(str2)).elements())
    if len(diff) == 1:
        print(string1, "is a step word of", string2)
    else:
        print (string1, "is not a stepword of", string2)

print(StepWord("listens", "silent"))

