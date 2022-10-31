# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:44:59 2022

@author: DISRCT
"""

def verificaBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return "É bissexto"
    elif ano % 100 == 0 and ano % 400 == 0:
        return "É bissexto"
    else:
        return "Não é bissexto"

ano = int(input("Ano: "))

print(f"O ano {ano} {verificaBissexto(ano)}")