#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:14:37 2020
Ejercicio 1
@author: samuel
"""
def pedida ():
    print("Programa para resolver chicharroneras\n ")
    A = int(input("Digite a: "))
    B = int(input("Digite b: "))
    C = int(input("Digite c: "))
    
    calculos(A,B,C)

"""
a,b,c = pedida()
print(f"{a} y {b} y {c}")
"""
def calculos (a, b, c):
    levar = (a**3 * (b**2 - 2*a*c)) / (2*b)
    print(f"{levar}")
    
pedida()