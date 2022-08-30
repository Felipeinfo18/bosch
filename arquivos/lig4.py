# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:36:04 2022

@author: disrct
"""
from colorama import Fore
import time
import os

matriz = [[" ", " ", " ", " ", " ", " ", " "] for i in range(6)]
vez = 1

def limpaTela():
    print("\n" * 25)

def mostraTabuleiro(matriz):
    # Mostra o tabuleiro 5x7
    print("      1   2   3   4   5   6   7")
    for lin in range(6):
        print("    |", end="")
        for col in range(7):
            if matriz[lin][col] == 'x':
                print(Fore.BLUE+" O ", end="")
            elif matriz[lin][col] == 'c':
                print(Fore.RED+" O ", end="")
                
            else: print(f" {matriz[lin][col]} ", end="")
            
            print(Fore.RESET+"|", end="")
        print()    

while True:    
    jogada = 0
    if vez == 1:
        print(Fore.BLUE+"           Jogador 1")
        
    elif vez == 2:
        print(Fore.RED+"            Jogador 2")

    print(Fore.RESET)
    
    mostraTabuleiro(matriz)
    
    while True:            
        if vez == 1:
            jogada = int(input("Jogada: "))
            
            if (jogada > 0 and jogada < 8) and matriz[0][jogada-1] == " ": 
                matriz[0][jogada-1] = 'x'
                break
       
        elif vez == 2:
            jogada = int(input("Jogada: "))
            if (jogada > 0 and jogada < 8) and matriz[0][jogada-1] == " ": 
                matriz[0][jogada-1] = 'c'
                break
    
    for i in range(6):
        if matriz[i][jogada-1] == " ":
            if vez == 1:
                matriz[i][jogada-1] = "x"
            else:
                matriz[i][jogada-1] = "c"
                           
            matriz[i-1][jogada-1] = " "
            
            mostraTabuleiro(matriz)
            
            time.sleep(0.2)
            limpaTela()
            
    if vez == 1:
        vez = 2
    elif vez == 2:
        vez = 1
        
    
