# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:01:13 2022

@author: mmfor
"""

'''
Examples for Functions
'''
import numpy as np
def fun1 (a,b):
    squares=a**2 + b**2
    c=np.sqrt(squares)
    return c
print(fun1(6,4))

#anonymous function
cubes=lambda x: x**3