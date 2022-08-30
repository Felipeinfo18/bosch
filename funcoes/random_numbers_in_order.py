# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:36:07 2022

@author: DISRCT
"""

import random

def preenche(minimo, maximo, tamanho):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(minimo, maximo))
    return lista

def ordena(lista):
    ordenada = []
    
    for i in range(0, len(lista)):
        ordenada.append(min(lista))
        lista.remove(min(lista))
        
    return ordenada

while True:
    inferior = int(input("Digite o limite inferior: "))
    superior = int(input("Digite o limite superior: "))
    tamanho = int(input("Digite o tamanho da lista: "))
    
    lista = preenche(inferior, superior, tamanho)
    print(f"LISTA: {lista}")
    lista = ordena(lista)
    print(f"LISTA ORDENADA: {lista}")
    
    if int(input("Digite 0 para sair do programa: ")) == 0:
        break