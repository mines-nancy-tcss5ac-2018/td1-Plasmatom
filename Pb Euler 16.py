# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def solve(n):
    """Solve the 16th Euler problem
    Return the number of digit"""
    s=0
    for digit in str(2**n):
        s+=int(digit)
    return s

assert(solve(15)==26)
print(solve(1000))