# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:41 2022

@author: disrct
"""

while True:
    print("""
          1 - Cadastrar 
          2 - Exibir
          3 - Sair""")
    escolha = int(input("> "))
    
    if escolha == 1:
        f = open("notasAlunos.txt", 'a')
        nome = input("Nome do aluno: ")
        notas = input("Insira 4 notas do aluno: ").split()
        
        f.write(nome + "#")
        f.write(str(notas) + "\n")
        f.close()
    elif escolha == 2:
        print("Alunos: ")
        with open("notasAlunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                linha = linha.split("#")
                nome = linha[0]
                print(nome)
                
        aluno = input("Nome do Aluno: ")
            
        with open("notasAlunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                linha = linha.split("#")
                nome = linha[0]
                notas = linha[1]
                notas = list(notas)
                notas.remove("[")
                notas.remove("]")
                notas = [item.replace(',', '') for item in notas]
                notas = [item.replace(' ', '') for item in notas]
                notas = [item.replace("'", '') for item in notas]
                notas = [item.replace("\n", '') for item in notas]
                notas = list(filter(None, notas))
    
                notasInteiras = []
                
                for nota in notas:
                    notasInteiras.append(int(nota))
                    
                if aluno == nome:
                    soma = 0.0
                    for nota in notasInteiras:
                        soma += nota
                    soma = soma / len(notasInteiras)
                    print(f"A média do aluno {nome} é {soma}")
    
    elif escolha == 3:
          break
