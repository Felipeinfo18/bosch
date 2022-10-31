# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:01:58 2022

@author: DISRCT
"""
import math

def calcula(valor = 0):
    raiz = math.sqrt(valor)
    quadrado = math.pow(valor, 2)
    inverso = 1/valor
    fatorial = math.factorial(valor)
    
    return raiz, quadrado, inverso, fatorial
    
def printa(valor = (0, 0, 0, 0)):
    print(f"""
              =================================
              Raiz quadrada: {valor[0]}

              Quadrado: {valor[1]}

              Inverso: {valor[2]}

              Fatorial: {valor[3]}
              ================================
          """)

while True:
    printa(calcula(int(input("Digite um valor: "))))
    if int(input("Digite 0 para sair")) == 0:
        break

