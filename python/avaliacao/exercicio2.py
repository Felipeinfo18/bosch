# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:08:18 2022

@author: disrct
"""

times = {1: ["Palmeiras", 30], 2: ["Corinthians", 24], 3: ["Fluminense", 17], 4: ["Vasco da Gama", 12]}

rodadas = int(input("Insira o número de rodadas: "))

for i in range(1, len(times) + 1):    
    for l in range(rodadas):
        print(f"Resultado da partida para {times.get(i)[0]}")
        print("""
              1 - Vitória
              2 - Derrota
              3 - Empata""")
              
        resultado = int(input())
        
        if resultado == 1:
            times.get(i)[1] += 3
        elif resultado == 2:
            times.get(i)[1] += 0
        elif resultado == 3:
            times.get(i)[1] += 1
    
maior = 0
time = []

for i in range(1, len(times) + 1):
    if times.get(i)[1] > maior:
        maior = times.get(i)[1]
        time = times.get(i)
    
print(f"O time com maior pontuação é o {time[0]} com {time[1]}")
        