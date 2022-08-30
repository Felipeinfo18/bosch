# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:21:40 2022

@author: disrct
"""
import unidecode

menu = {"Hamburguer": 10, "HotDog": 6.5, "Salada": 4, "Suco": 4, "Refrigerante": 4.5, "Água": 2}

print(f"Menu FastFood\n{menu}")

valor1 = input("Digite a comida que você deseja: ")
valor2 = input("Digite a bebida que você deseja: ")

print(f"O valor total é de: {menu[valor1]+menu[valor2]}")