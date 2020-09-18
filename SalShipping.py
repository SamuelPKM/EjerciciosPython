#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:26:47 2020

@author: samuel
"""

def Ground_Shipping(weight,Premium):
    Flat_Charge = 20
    if (weight <= 2):
        Price_PP = 1.5
    elif (weight <=6 and weight >2):
        Price_PP = 3
    elif (weight >6 and weight<=10):
        Price_PP = 4
    elif (weight > 10):
        Price_PP = 4.75
    if (Premium == 'Yes' or Premium == "yes"):
        Flat_Charge = 150
    cost = weight * Price_PP + Flat_Charge    
    return cost

def Drone_Shipping(weight):
    Flat_Charge = 0
    if (weight <= 2):
        Price_PP = 4.5
    elif (weight <=6 and weight >2):
        Price_PP = 9
    elif (weight >6 and weight<=10):
        Price_PP = 12
    elif (weight > 10):
        Price_PP = 14.25
    cost = weight * Price_PP + Flat_Charge    
    return cost
print (str(Ground_Shipping(8.4,"yes")))
print (str(Drone_Shipping(1.5)))