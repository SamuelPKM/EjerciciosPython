#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 01:18:23 2020

@author: samuel
"""

import re

print('Hola, indica el numero de proseores que tienes, seguido por el numero de alumnos que votaran')
linea1 = input()

array = []
for r in re.finditer('\d+',linea1):
    array[r] = r.group(0)

print('Tu tienes'+ array[0]+ 'Profesores')