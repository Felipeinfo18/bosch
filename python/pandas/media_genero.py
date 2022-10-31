# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:40:10 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

def preenche_idade(linha):
    idade = linha["Age"]
    sexo = linha["Sex"]
    global media_mulher
    global media_homem
    
    if pd.isnull(idade): #funcao padrão do pandas para verificar se na linha tem dado nulo
        
        if sexo == "female":
            return media_mulher
        else:
            return media_homem
        
    else:
        return idade

media_mulher = titanic[titanic.Sex == "female"].Age.mean()
media_homem = titanic[titanic.Sex == "male"].Age.mean()    

idades_preenchidas = titanic.apply(preenche_idade,axis=1)
    
titanic["AgeFillNaSexMean"] = idades_preenchidas

print(titanic)
print(f"Idade média das mulheres: {media_mulher}\nIdade média dos homens: {media_homem}")