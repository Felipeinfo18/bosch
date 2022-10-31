# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:02:01 2022

@author: disrct
"""

def verificaTriangulo(ladoA, ladoB, ladoC):
    if abs(ladoB - ladoC) < ladoA and ladoA < (ladoB + ladoC):
        if abs(ladoA - ladoC) < ladoB and ladoB < (ladoA + ladoC):
            if abs(ladoA - ladoB) < ladoC and ladoC < (ladoA + ladoB):
                return True
    return False

def classificaTriangulo(ladoA, ladoB, ladoC):
    if ladoA == ladoB:
        if ladoC == ladoB:
            return 2
        return 1
    elif ladoB == ladoC:
        if ladoA == ladoB:
            return 2
        return 1
    elif ladoA == ladoC:
        if ladoA == ladoB:
            return 2
        return 1
    return 0

ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))

if verificaTriangulo(ladoA, ladoB, ladoC):
    ladosIguais = classificaTriangulo(ladoA, ladoB, ladoC)
    if ladosIguais == 0:
        print("É um triângulo escaleno")
    elif ladosIguais == 1:
        print("É um triângulo isósceles")
    elif ladosIguais == 2:
        print("É um triângulo equilátero")
       
else:
    print("Não é um triangulo!")