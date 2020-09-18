#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:39:53 2020
Ejercicio 2 Operadores logicos
@author: samuel
"""

def Predator(a,b):
    estatus = ((3+5*8)<3) and (((-6/3) * 4 + 2 < 2)) or (a>b)
    return estatus

A = int(input("Digita a: "))
B = int(input("Digita b: "))

print(f"{Predator(A,B)}")