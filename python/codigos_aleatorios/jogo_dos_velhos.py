# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:14:09 2022

@author: disrct
"""

#Jogo da velha
print("Jogo da velha")
turno = 1
linha1 = [" ", " ", " "]
linha2 = [" ", " ", " "]
linha3 = [" ", " ", " "]
linha = 0
coluna = 0
marca = "X"
gameover = 0

while True:
    for i in range(0, 3):
        print(linha1[i], end="")
        if i != 2:
            print("|", end="")
    print("\n-----")
    for i in range(0, 3):
        print(linha2[i], end="")
        if i != 2:
            print("|", end="")
    print("\n-----")
    for i in range(0, 3):
        print(linha3[i], end="")
        if i != 2:
            print("|", end="")    
        
    #Verifica GameOver
    gameover = 1
    
    for i in range(0, 3):
        if linha1[i] == " ":
            gameover = 0
        if linha2[i] == " ":
            gameover = 0
        if linha3[i] == " ":   
            gameover = 0
            
    if gameover:
        break
    
    if turno == 1:
       print("\nVez do jogador 1")
       marca = "X"
       turno = 2
    else:
        print("\nVez do jogador 2")
        marca = "O"
        turno = 1
       
    linha = int(input("Insira a linha: "))        
    
    coluna = int(input("Insira a coluna: "))

    if linha == 1:
        linha1[coluna - 1] = marca
    if linha == 2:
        linha2[coluna - 1] = marca
    if linha == 3:
        linha3[coluna - 1] = marca

