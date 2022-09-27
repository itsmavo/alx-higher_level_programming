#!/usr/bin/python3
""" pascal triangle """

def pascal_triangle(n):
    """ implementation """
    tri = []
    prev = []
    for i in range(n):
        Next = [1] + [sum(prev[num:num + 2]) for num in range (len(prev) - 1)]
        if i > 0:
            Next = Next + [1]
        tri.append(Next)
        prev = Next
    return tri
