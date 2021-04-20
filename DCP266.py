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
    return (EqualLength)
            
    
dictword = DictionaryLoop("silent", ["listens", "cat", "shreya", "alaisha"])


def StepWord(string1, dictword):
    str1 = list(string1)
    for i in dictword:
        str2 = list(i)
        diff = list((Counter(str2)-Counter(str1)).elements())
        if len(diff) == 1:
            print(i, "is a step word of", string1)
        else:
            print (i, "is not a stepword of", string1)

print(StepWord("silent", dictword))

