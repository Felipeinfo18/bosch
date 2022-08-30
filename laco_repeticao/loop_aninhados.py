# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:54:41 2022

@author: disrct
"""
while True:
    num = int(input("Insira um número positivo inteiro: "))
    if num > 0:
        break

#laços de repetição aninhados
for i in range(0, num):
    for l in range(0, num):
        print("x ", end="")
    print()
