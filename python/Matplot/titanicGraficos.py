# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:54:50 2022

@author: disrct
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titanic = pd.read_csv("data/titanic.csv")
sobreviventes = titanic.Survived[titanic.Survived == 1].count()
mortos = titanic.Survived[titanic.Survived == 0].count()

# =============================================================================
# plt.rcParams["figure.figsize"] = (25, 20)
# plt.rcParams.update({'font.size': 40})
# =============================================================================

# =============================================================================
# plt.title("Quantidade de pessoas sobreviveram ou não.")
# plt.xticks(rotation = '90')
# 
# help(plt.bar)
# print(irmaos)
# 
# plt.bar(["Survived", "Not Survived"], [sobreviventes, mortos], width = 0.4, color = 'pink', edgecolor = 'black', linewidth = 3)
# =============================================================================
# =============================================================================
# plt.figure(figsize=(20, 18))
# irmaos = titanic.groupby("SibSp").PassengerId.count()
# pais = titanic.groupby("Parch").PassengerId.count()
# titanic["Relatives"] = titanic.SibSp + titanic.Parch
# total = titanic.groupby("Relatives").count()
# 
# total = total.PassengerId
# 
# plt.plot(total, marker = 'o', label = 'Total de parentes', linewidth = 5, markersize = 15)
# plt.plot(irmaos, marker = 'x', label = 'Número de irmãos/conjuges a bordo', linewidth = 5, markersize = 15)
# plt.title("Quantidade de pessoas por quantidade de parentes à bordo")
# plt.plot(pais, marker = 'v', label = "Número de pais/filhos a bordo", linewidth = 5, markersize = 15)
# plt.legend()
# plt.grid()
# plt.ylabel("Quantidade de pessoas")
# plt.xlabel("Quantidade de parentes")
# 
# =============================================================================
plt.figure(figsize=(35, 20))
plt.xticks(np.arange(0, 61, 3))
plt.yticks(np.arange(2.5, 20, 2.5))
plt.axis([0, 60, 0, 19])

plt.title("Quantidade de pessoas por idade")
plt.xlabel("Idade")
plt.ylabel("Quantidade de pessoas")

pessoasIdadeHomem = titanic[titanic.Sex == "male"].groupby("Age")
pessoasIdadeHomem = pessoasIdadeHomem.PassengerId.count()
pessoasIdadeMulher = titanic[titanic.Sex == "female"].groupby("Age")
pessoasIdadeMulher = pessoasIdadeMulher.PassengerId.count()

plt.scatter(pessoasIdadeHomem.index, pessoasIdadeHomem, s=600, marker = 'o', label = "Homem")
plt.scatter(pessoasIdadeMulher.index, pessoasIdadeMulher, c='orange', s=600, marker = 'o', label = "Mulher")












plt.legend()