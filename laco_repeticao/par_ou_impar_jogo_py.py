# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:41:29 2022

@author: disrct
"""
import random

record = 0

print("--------------NOVO-JOGO---------------")

while True:   
    vitorias = 0
    
    while True:
        numero = int(input("Digite um número: "))
    
        escolha = input("PAR OU IMPAR? ").lower()
        
        aleatorio = random.randint(0, 5)
        
        print(f"O computador jogou: {aleatorio}")
        print(f"RESULTADO: {numero + aleatorio}\n")
    
        if (numero + aleatorio) % 2 == 0 and escolha == "par":
            print("Você ganhou!")
            vitorias += 1
        elif (numero + aleatorio) % 2 != 0 and escolha == "impar":
            print("Você ganhou!")
            vitorias += 1
        else: 
            print("Você perdeu!")
            break
        
            
    print(f"VITÓRIAS: {vitorias}")
    if vitorias > record:  record = vitorias
    print(f"\nRECORD: {record}")
    if int(input("Digite 0 para sair ")) == 0:
        break
