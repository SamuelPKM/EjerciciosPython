#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:27:27 2020

@author: samuel

"""
import numpy as np;

def iniciarMatriz():
    A = str(input("Escribe las Filas y Columnas "))

    print(f"La matriz sera de {A[0]} {A[2]} ")

    F = int(A[0])
    C = int(A[2])
    if (F>0 and F<1000 and C>1 and C<1000):
        matriz = np.zeros((F,C))
        return matriz,F,C
    else:
        print ("No esta permitido ese rango de valores")
        


def PedidaDatosMatriz(matriz,C,R):
    for r in range (0,R):
        for c in range (0,C):
            print(f"Dame los datos de la posicion [{r+1}][{c+1}] ")
            matriz[r,c] = input()
    return matriz;

def RotacionLista(Lista):
    rotadaLista = []
    for i in range(len(Lista[0])):
        rotadaLista.append([])
        for j in range(len(Lista)):
            rotadaLista[i].append(Lista[len(Lista)-1-j][i])
    return rotadaLista

def PedidaLista(matriz,R,C):
    Lista = []
    for i in range(0,R):
        Lista.append([])
        for j in range(0,C):
            Lista[i].append(input())
    return Lista

def RotacionMatriz(matriz):
    rotada = np.rot90(matriz, k=3)
    #print(rotada)
    return rotada

def ImprimirLista(Lista,R):
    for i in range(R):
        print (Lista[i])

def Comparacion(matriz,Lista,R,C):
    for i in range (0,R):
        for j in range (0,C):
            if(Lista[i][j] == 'X'):
                print(matriz[i][j])
                
                
try:    
    matrizA,C1,R1 = iniciarMatriz()
    matrizA = PedidaDatosMatriz(matrizA, R1, C1)    
    print(matrizA)
    #rotada = RotacionMatriz(matrizA)
    #print(rotada)
    Lista1 = PedidaLista(matrizA,R1,C1)
    ImprimirLista(Lista1, R1)
    ListaAux = Lista1
    Nrot = int(input("Cuantas veces quieres rotar la matriz? "))
    for i in range(0,Nrot):
        ListaRotada = RotacionLista(Lista1)
        Lista1 = ListaRotada
    
    print(matrizA)
    print("Matriz original ")
    ImprimirLista(Lista1,R1)
    print("Matriz rotada ")
    ImprimirLista(ListaAux, R1)
    print("Las coincidencias con las 'x' son ")
    Comparacion(matrizA,Lista1,R1,C1)
except :
   print("\n Sin ejecucion exitosa")