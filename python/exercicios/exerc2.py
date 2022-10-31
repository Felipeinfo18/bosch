# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:30:23 2022

@author: DISRCT
"""

matheus = 1.5
jose = 1.1
anos = 0

while True:
    anos += 1
    matheus += 0.02
    jose += 0.03   
    
    if jose > matheus:
        break
    
print(f"José será maior que Matheus em {anos} anos")