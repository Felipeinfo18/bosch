# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:47:58 2022

@author: disrct
"""
#Aula 02 - Laços de repetição e condicionais

print("JOGO DA ADVINHAÇÃO\n----------------------------------------------------")
numero_secreto = 42
palpite = ""

while palpite.isdigit() == False:
    palpite = input("Digite seu palpite: ")

if int(palpite) == 42:
    print("Você Acertou!")
else:
    print("Você Errou!")