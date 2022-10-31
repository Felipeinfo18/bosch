# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:50:32 2022

@author: disrct
"""
#Usando um contador com delay
import time

def contador(inicio, fim, passo):
    if fim < inicio:
        fim -= 1
        # Se o inicio for maior que fim e o passo estiver positivo, é necessário invertar para o contador 
        # funcionar neste caso
        if passo > 0: passo *= -1
    else: fim += 1
    
    print(f"\n---------- CONTADOR PASSO: {abs(passo)} INICIO: {inicio} FIM: {fim} ------------")
    
    for i in range(inicio, fim, passo):
        print(i)
        time.sleep(1)

while True:
    #Leitura dos dados dentro da função
    contador(int(input("Digite o início do contador: ")), 
             int(input("Digite o final do contador: ")), 
             int(input("Digite o passo do contador: ")))
    
    #Exit do programa
    if int(input("Digite 0 para sair: ")) == 0:
        break
    
# contador ( VALOR INICIAL, VALOR FINAL, VALOR INCREMENTADO DO INICIO AO FIM )
# =============================================================================
# 
# contador(20, 0, 2)
# contador(0, 105, 5)
# contador(96, 52, 2)
# contador(3, 41, 1)
# contador(75, 15, 5)
# contador(390, 39, 10)
# 
# =============================================================================
