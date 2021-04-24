#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:01:54 2021

@author: Alaisha Naidu
Name: Daily Coding Problem 270
"""
#270

edges = [
    [0, 1, 5],
    [0, 2, 3],
    [0, 5, 4],
    [1, 3, 8],
    [2, 3, 1],
    [3, 5, 10],
    [3, 4, 5]]

def find_time(N, nodes):
    if N == 0:
        return 0

    D = nodes[N]
    time = list()
    for a, b in D:
        print(a,b)
        dist = b + find_time(a, nodes)
        time.append(dist)

    return min(time)


def shortest_path(edges, N): #takes list of edges and end node, N
    nodes = dict() #create an empty dictionary
    for edge in edges:
        start, end, time = edge
        if end not in nodes:
            nodes[end] = list()
        nodes[end].append((start, time))

    time = list()
    for n in set(range(1, N + 1)):
        dist = find_time(n, nodes)
        time.append(dist)

    return max(time)

print(shortest_path(edges, 5))



