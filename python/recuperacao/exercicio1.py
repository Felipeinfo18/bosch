# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:18:18 2022

@author: disrct
"""

lista = ['1_palmeiras', '2_coritiba', '1_corinthians', '3_juventude', '2_fluminense', '3_bahia', '1_cuiaba', '2_cascavel', '3_ponte preta', '2_parana clube', '3_voltaredonda']

primeira_div = []
segunda_div = []
terceira_div = []

for i in range(len(lista)):
    parte1 = lista[i].split('_')[0]
    parte2 = lista[i].split('_')[1]
    
    if parte1 == '1':
        primeira_div.append(parte2)
    elif parte1 == '2':
        segunda_div.append(parte2)
    elif parte1 == '3':
        terceira_div.append(parte2)
        
        
print(f"""
      Primeira Divisão: {primeira_div}
      Segunda Divisão: {segunda_div}
      Terceira Divisão: {terceira_div}
      """)
      