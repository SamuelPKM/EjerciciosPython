#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:29:21 2020

@author: samuel
"""
import numpy as np
import sys

def iniciarMatriz():
    A = str(input("Escribe el N y M "))

    print(f"La matriz sera de {A[0]} {A[2]} ")

    F = int(A[0])
    C = int(A[2])
    matriz = np.zeros((F,C))
    return matriz,F,C

def Multiplicacion(matrizA,matrizB, C1,R1,C2,R2):
    if (C1 != R2):
        print("No se puede hacer la operacion")
        sys.exit()
    else:
            matrizR = np.zeros((C1,R2))    
            
            for r in range (0,R1):
                for c in range (0,C1):
                    matrizA[r,c] = input(f"Elemento de la posicion [{r+1},{c+1}] ")
           
            for r in range (0,R2):
                for c in range (0,C2):
                    matrizB[r,c] = input(f"Elemento de la posicion [{r+1},{c+1}] ")
           
            for r in range (0,R2):
                for c in range (0,C2):
                    for k in range (0,R2):
                        matrizR[r,c] += matrizA[r,k]*matrizB[k,c]    
            print(matrizR)


matrizA,C1,R1 = iniciarMatriz()
for r in range (0,R1):
    for c in range (0,C1):
        matrizA[r,:] = input()
#Multiplicacion(matrizA,C1,R1,matrizB,C2,R2)"""


print(matrizA)

# matrizB,C2,R2 = iniciarMatriz()    