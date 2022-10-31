# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:09 2022

@author: disrct
"""
class erro(Exception):
    pass

def calculaAlgarismos(numero):
    soma = 0.0
    
    while numero >= 1:
        valor = float(numero / 10 - int(numero / 10))
        valor *= 10
        soma += int(valor)
        numero = int(numero / 10)
    return soma

while True:
    try:
        numero = int(input("Insira um número maior que zero: "))
    
        if numero < 0:
            raise erro
    except erro:
        print("Número inválido")
        break
    else:
        print(f"A soma dos algarismos é igual a {round(calculaAlgarismos(numero))}")
        break