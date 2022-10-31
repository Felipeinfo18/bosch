# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:30:01 2022

@author: DISRCT
"""
import math

def verificaQuadradoPerfeito(valor):
    quadrado = math.sqrt(valor)
    if quadrado == float(math.ceil(quadrado)) or quadrado == float(math.floor(quadrado)):
        return "É um quadrado perfeito"
    else:
        return "Não é um quadrado perfeito"
    
while True: 
    try:
        numero = int(input("Número: "))
        if numero > 0: break
    except ValueError:
        pass
    
print(f"O número {numero} {verificaQuadradoPerfeito(numero)}")