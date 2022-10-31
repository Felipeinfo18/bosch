# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:33 2022

@author: disrct
"""

def converteBinario(senha):
    codigo = []
    separador = [list(letra) for letra in senha]
    for caractere in separador:
        caractere = caractere[0]
        if caractere.isalpha():
            caractere = ord(caractere) - 97
            if caractere >= 10:
                parte1 = float(caractere/10)
                parte2 = int(caractere/10)
                parte1 = float(parte1 - parte2) * 10
                parte1 = int(parte1)
                parte1 = converteBin(parte1)
                codigo.append(preencheZero(parte1)+"_")
                
                parte2 = converteBin(parte2)
                codigo.append(preencheZero(parte2)+"_")
            else:
                valor = caractere
                valor = converteBin(valor)
                preencheZero(valor) 
                codigo.append(preencheZero(valor)+"_")
        else:        
            if caractere.isalnum() == False:
                caractere = 0
            
            valor = caractere
            valor = converteBin(valor)
            codigo.append(preencheZero(valor)+"_")
            
    return codigo

def converteBin(valor):
    valor = bin(int(valor)) 
    valor = str(valor)
    valor = valor.split('b')
    valor = valor[1]
    return int(valor)
            

def preencheZero(numero):
    if numero < 10:
        numero = "000" + str(numero)
    elif numero < 100:
        numero = "00" + str(numero)
    elif numero < 1000:
        numero = "0" + str(numero)
    
    return str(numero)
    
senha = input("Insira a senha para ser codificada\n")

binario = converteBinario(senha.lower())
binario[-1] = binario[-1].replace("_", "")
print("Codificação = ", end="")
for i in binario:
    print(i, end="")