# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:42:00 2022

@author: DISRCT
"""

import pandas as pd

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""

    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

titanic = pd.read_csv("data/titanic.csv")

# Tranformando dados com apply

# Aplicando uma função aos dados para transformar a idade em faixas etárias.
# O resultado do apply é uma Série.
def faixa_etaria(linhas):
    idade = linhas["Age"]
    if idade < 12:
        return "criança"
    elif idade >=12 and idade < 18:
        return "adolescente"
    elif idade >=18 and idade < 65:
        return "adulto"
    elif idade >= 65:
        return "idoso"
    else:
        return "nada"
        
# Criamos a coluna "faixa_etaria" onde atribuímos o valor da Série
# resultante do apply

titanic["faixa_etaria"] = titanic.apply(faixa_etaria, axis=1)

mortos = titanic[titanic["Survived"] == 0]
vivos = titanic[titanic["Survived"] == 1]

print(f"Nº de Sobreviventes: {vivos.Survived.count()}\nNº de Mortos: {mortos.Survived.count()}")

mulheres_criancas_mortas = mortos.Survived[(titanic["faixa_etaria"] == "criança") | (titanic["Sex"] == "female")].count()
mulheres_criancas_vivas = vivos.Survived[(titanic["faixa_etaria"] == "criança") | (titanic["Sex"] == "female")].count()

print(f"{mulheres_criancas_vivas} dos sobreviventes eram mulheres ou crianças")
print(f"{mulheres_criancas_mortas} dos mortos eram mulheres ou crianças")

print(f"{calculate_percentage(mulheres_criancas_vivas, vivos.Survived.count())} dos sobreviventes eram mulheres ou crianças")
print(f"{calculate_percentage(mulheres_criancas_mortas, mortos.Survived.count())} dos mortos eram mulheres ou crianças")
