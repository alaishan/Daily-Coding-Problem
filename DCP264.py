#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:42:19 2021

@author: Alaisha Naidu
Name: Daily Coding Problem 264
Credits: Wikipedia

"""

from typing import Iterable, Union, Any
def de_bruijn(k: Union[Iterable[Any], int], n: int) -> str:
    """de Bruijn sequence for alphabet k
    and subsequences of length n, denoted by B(k, n)
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int): #isinstance returns true if the k is an int
        alphabet = list(map(str, range(k))) #map is used in place of a loop
    else:
        # While any sort of list becomes used as it is
        alphabet = k #otherwise checks if k is a string
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)


print(de_bruijn(2, 3))
print(de_bruijn("abcd", 2))