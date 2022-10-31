# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:18 2022

@author: disrct
"""

gabarito = ['a', 'c', 'a', 'd', 'c', 'b', 'b', 'd', 'c', 'a']
respostas = []

for i in range(len(gabarito)):
    respostas.append(input(f"Qual a sua resposta para a questão {i + 1}? "))
    
conta = 0
erradas = []

for i in range(len(respostas)):
    if respostas[i] == gabarito[i]:
        conta += 1
    else:
        erradas.append(i+1)
        
print(f"Sua nota foi {conta}")
if len(erradas) > 0:
    print(f"Você errou as respostas: {erradas}")