# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:54:01 2022

@author: disrct
"""

qntd = input('Quantas frases deseja verificar? ')

palindromos = []

for i in range(int(qntd)):
    frase = input(f'Insira a {i+1}º frase\n')
    
    contrario = []
    fraseSemEspaco = frase.replace(' ', '')
    for i in range(len(fraseSemEspaco) - 1, -1, -1):
        contrario.append(fraseSemEspaco[i])
            
    if ''.join(contrario).lower() == fraseSemEspaco.lower():
        palindromos.append(frase)
        
        
print('São palíndromos:\n')

for i in range(len(palindromos)):
    print(palindromos[i])
    
