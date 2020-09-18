#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:55:15 2020
Ejercicio 3 Par o impar de ambos numeros
@author: samuel
"""
def Valad (a,b):
    if (a%2 == 0) and (b%2 == 0):
        print("Ambos son pares")
    elif((a%2 == 0)):
            print(f"{a} es par y {b} es impar")
    elif((b%2 == 0)):
            print(f"{a} es impar y {b} es par")
    else:
        print("Ninguno es par, ambos son impares")
        
A = int(input("Digita el numero A "))
B = int(input("Digita el numero B "))
Valad(A,B)