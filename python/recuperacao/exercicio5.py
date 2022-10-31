# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:24:43 2022

@author: disrct
"""

def saque(valor):
    notas = {}
    while int(valor) > 1:
        if int(valor) > 100:
            notas["R$100,00"] = int(int(valor) / 100)
            valor = valor-(100*(int(int(valor) / 100)))
        elif int(valor) > 50:
            notas["R$50,00"] = int(int(valor) / 50)
            valor = valor-(50*(int(int(valor) / 50)))
        elif int(valor) > 10:
            notas["R$10,00"] = int(int(valor) / 10)
            valor = valor-(10*(int(int(valor) / 10)))
        elif int(valor) > 5:
            notas["R$5,00"] = int(int(valor) / 5)
            valor = valor-(5*(int(int(valor) / 5)))
        elif int(valor) > 1:
            notas["R$1,00"] = int(int(valor) / 1)
            valor = valor-(1*(int(int(valor) / 1)))

    return notas
while True:
    valor = int(input("Insira qual valor deseja sacar: (mínumo R$10,00)\n"))
    
    if valor > 10 and valor < 600:
        break
    else:
        print("Valor não correspondente")
        
dinheiro = saque(valor)

print('Notas para saque: ')

for chave, valor in dinheiro.items():
    print(f"{valor} notas de {chave}")