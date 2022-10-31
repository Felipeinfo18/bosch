# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:40:45 2022

@author: disrct
"""

import random
import unidecode

def mostraJogo():
    global palavra
    global codificada

    for i in range(len(codificada)):
        print(f"{codificada[i]} ", end="")    

def listAlphabet():
    return list(map(chr, range(97, 123)))

class erro(Exception):
    pass

palavras = []

with open("forca.txt", "r") as arquivo:
    for linha in arquivo:
        palavras.append(linha)

while True:
    placar = 6
    
    
    alfabeto = listAlphabet()
    palavra = palavras[random.randint(0, len(palavras)-1)]
    hold = palavra
    codificada = ""
    
    for i in range(len(palavra)-1):
        codificada += "_"
        
    escolha = int(input("""
          Jogo da Forca
          
          [1] - Iniciar Jogo
          [2] - Sair
          > """)) 
    
    if escolha == 1:
        while True:
            while True:
                try:
                    print("     ", end='')
                    mostraJogo()
                    letra = input("\n     Insira uma letra: ")
                    existe = False

                    if letra.isalpha() == False or len(letra) > 1:
                        raise erro()
                    else:
                        for i in range(len(alfabeto)):
                            if alfabeto[i] == letra:
                                alfabeto[i] = ''
                                existe = True
                        if existe: break
                        else: print("     Essa letra já foi usada!")
                except erro:
                    print("     Valor inválido!")
            if (letra in hold) == False:
                placar -= 1
            
            if placar == 0:
                print("     Você perdeu!!")
                print(f"     A palavra era {palavra}")
                break
            
            while letra in hold:
                indice = hold.find(letra)
                hold = hold[:indice] + ' ' + hold[indice + 1:]
                codificada = codificada[:indice] + letra + codificada[indice + 1:]
            if codificada == palavra:
                print("      Parabéns você ganhou!!")
                break
            
    else:
        break