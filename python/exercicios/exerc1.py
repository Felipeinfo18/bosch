# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:11:35 2022

@author: DISRCT
"""

def calculaIMC(peso, altura):
    return (peso/altura**2)

def classificaIMC(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc >= 18.5 and imc <= 24.9:
        return "Normal"
    elif imc >= 25 and imc <= 29.9:
        return "Sobrepeso"
    elif imc >= 30 and imc <= 39.9:
        return "Obesidade"
    if imc >= 40:
        return "Obesidade Grave"            

peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

imc = float(calculaIMC(peso, altura))

print(f"O IMC da pessoa é {imc: .2f}")
print(f"E está classificada como {classificaIMC(imc)}!")-

















































