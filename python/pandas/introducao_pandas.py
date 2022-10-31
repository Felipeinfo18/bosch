# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:48:27 2022

@author: DISRCT
"""

import pandas as pd
titanic = pd.read_csv("data/titanic.csv", sep=",")

# print(titanic[titanic.columns[:-1]])

# =============================================================================
# filtroLista = titanic.loc[:, ['Age', 'Pclass']]
# 
# print(filtroLista.describe())
# =============================================================================

# =============================================================================
# Funções do Panda
# iloc[valor: valor, valor: valor] [linha, coluna]
# loc[valor: valor, ["valor"]] [linha, coluna]
# describe() Gera descrição do dataframe
# mean() linha da descrição 
# std() linha da descrição
# head(param: numero limite da linha que vai mostrar)
# fillna(valor) preenche linhas com nan
# dropna(valor) exclui linhas com nan
# count_values() conta a quantidade de vezes que determinado valor se repetiu
# unique() pega o valores unicos no dataframe
# groupby(coluna) agrupa valores do dataframe com base num valor
# sort_values(valor) ordena os valores do dataframe baseado no valor
# =============================================================================
