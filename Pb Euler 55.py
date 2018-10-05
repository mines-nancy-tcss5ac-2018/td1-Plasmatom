# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:01:41 2018

@author: Louis
"""


def isPalindrome(n):
    nb=str(n)
    length=len(nb)
    if length%2==0:
        if nb[:length//2]==''.join(reversed(nb[length//2:])):
            return True
    else:
        if nb[:length//2]==''.join(reversed(nb[length//2+1:])):
            return True
    return False





def solve(n):
    """ Solve the 55th Euler problem
        Return the number of Lychrel numbers below 10000"""
    compteur=0
    for i in range(10000):
        a=i
        p=0
        for j in range(50):
            a+=int(''.join(reversed(str(a))))
            if isPalindrome(a):
                p=1
                break
        if p==0:
            compteur+=1
    return compteur

print(solve(10000))