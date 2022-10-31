# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:26 2022

@author: disrct
"""

import random

aleatorio = random.randint(1, 1000)
tentativas = 0

while True:
    numero = int(input("Tente acertar o número sorteado: "))

    tentativas += 1
    if numero == aleatorio: break
    
    if numero - aleatorio > 3:
        print("Muito alto")
    elif numero - aleatorio < -3:
        print("Muito baixo")
    else:
        print("Quase!!")
          
    print()

print(f"Parabéns você acertou!! O número é {aleatorio}")
print(f"Foram necessárias {tentativas} tentativas")   