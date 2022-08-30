# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:56:03 2022

@author: DISRCT
"""
class ValorDiferente(Exception):
    pass

def soma(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2
    
def mult(num1, num2):
    return num1*num2
    
def div(num1, num2):        

    try:
        num1/num2
    except ZeroDivisionError:
        print("Divisão impossível! Tente novamente!")
        return "ERRO"

    return num1/num2

def mostraResultado(valor):
    print(f"Resultado: {valor}")

print("============== CALCULADORA INFALÍVEL! ===============")

while True:
    while True:
        try:
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))
            break
        except ValueError:
            print("Valores inválidos! Tente novamente!")            

    verifica = True
    
    while verifica == True:

        verifica = True
        operacao = input("""
        Operações:
        1 - Adição
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        Digite a operação desejada: """)

        try:
            if int(operacao) == 1:
               mostraResultado(soma(num1, num2))
               break
            elif int(operacao) == 2:
               mostraResultado(sub(num1, num2))
               break
            elif int(operacao) == 3:
               mostraResultado(mult(num1, num2))
               break
            elif int(operacao) == 4:
               mostraResultado(div(num1, num2))
               break
            else:
                raise ValorDiferente
        except ValueError:
            print("Valores inválidos! Tente novamente!")

        except ValorDiferente:
            print("Insira um valor entre 1 e 4!")