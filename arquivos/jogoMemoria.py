# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 08:18:47 2022

@author: DISRCT
"""
import time
import random
import winsound
from colorama import Fore

#jogo da memoria

#Função que printa todo o campo
def mostraCampo(campo):    
    global cor

    print("=" * 50)

    for i in range(20):
        for l in range(50):
            if campo[i][l] == "#":
                aleatorizaCor()
                print(cor, end="")
            print(campo[i][l], end="")
            print(Fore.RESET, end="")
        print()
    print("=" * 50)

#Função que redefine o campo para vazio
def limpaCampo():   
    global campo
    for i in range(20):
        for l in range(50):
            campo[i][l] = " "

#Função que inicia os "#" dentro do campo
def iniciaValores(campo, valorAleatorio):
    for i in range(valorAleatorio):
        while True:
            x = random.randint(0, 49)
            y = random.randint(0, 19)
            
            if campo[y][x] == " ":
                campo[y][x] = "#"
                break   

#Função que "substitui" o system('cls') e limpa a tela
def limpaTela():
    print("\n" * 40)

#Função que aleatoriza o número de # dentro do campo
def aleatorizaValor():
    global valorAleatorio
    if escolha == 1: 
        valorAleatorio = random.randint(5, 10)
    elif escolha == 2: 
        valorAleatorio = random.randint(10, 20)
    elif escolha == 3: 
        valorAleatorio = random.randint(20, 30)

#Função que define uma cor aleatória para cada #
def aleatorizaCor():
    valor = random.randint(0, 7)
    global cor

    if valor == 0:
        cor = Fore.CYAN
    elif valor == 1:
        cor = Fore.RED
    elif valor == 2:
        cor = Fore.GREEN
    elif valor == 3:
        cor = Fore.LIGHTBLUE_EX
    elif valor == 4:
        cor = Fore.LIGHTWHITE_EX
    elif valor == 5:
        cor = Fore.YELLOW
    elif valor == 6:
        cor = Fore.MAGENTA
    elif valor == 7:
        cor = Fore.LIGHTYELLOW_EX
      
#Classe de erro para Exceptions
class Erro(Exception):
    pass

#Escopo das variáveis
campo = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "] for i in range(20)]
valorAleartorio = 0
pontuacao = 0
recorde = 0
cor = Fore.RESET

#Pega recorde dentro do arquivo texto e armazena na variável
with open('pontuacao.txt') as arquivo:
    for linha in arquivo:
        recorde = int(linha.split(":")[1])

#Inícia o jogo
while True:
    while True:
        try:
            print("""
                     =======================================
                                
                                 JOGO DA MEMÓRIA
                              
                          [1]   COMEÇAR NOVO JOGO
                          [2]        RECORDE
                          [3]         SAIR
                                  
                                feito por: Felipe
                     =======================================""")
            escolha = int(input("> "))
            if escolha > 0 and escolha < 4:
                break
                
        except Exception:
            pass
        
    #Opção 1 = Jogo
    if escolha == 1:
        pontuacao = 0
        while True:
            try:
# =============================================================================
#                 dificuldade 1 - Cada campo fica visivel durante apenas 0.5 sec mas possui entre 5 a 10 #
#                 dificuldade 2 - Cada campo fica visivel durante 1 sec mas possui entre 10 a 20 #
#                 dificuldade 3 - Cada campo fica visivel durante 1.5 sec mas possui entre 20 a 30 #
# =============================================================================
                limpaTela()
                print("""
                          =======================
                          Dificuldades:
                          [1] - Fácil
                          [2] - Intermediário
                          [3] - Modo HARD
                          ======================""")
                    
                escolha = int(input("> "))
                
                if escolha < 1 or escolha > 3:
                    raise Erro
                else:
                    break
            except Exception:
                print("Valor inválido! Tente novamente!")
            except Erro:
                print("Digite um valor entre 1 e 3!")
         
        limpaTela()
        print(Fore.LIGHTWHITE_EX+"            PREPARADO?")
        time.sleep(1)
        limpaTela()
        print(Fore.LIGHTWHITE_EX+"            VAI!"+Fore.RESET)
        time.sleep(1)
        
        while True:
            aleatorizaValor()
            while True:
                if escolha == 1:
                    for i in range(5):
                        limpaCampo()
                        iniciaValores(campo, valorAleatorio)
                        mostraCampo(campo)
                        winsound.Beep(2000, 4)
                        time.sleep(1)
                        limpaTela()
                elif escolha == 2:
                    for i in range(5):
                        limpaCampo()
                        iniciaValores(campo, valorAleatorio)
                        mostraCampo(campo)
                        winsound.Beep(2000, 4)
                        time.sleep(2)
                        limpaTela()
                elif escolha == 3:
                    for i in range(5):
                        limpaCampo()
                        iniciaValores(campo, valorAleatorio)
                        mostraCampo(campo)
                        winsound.Beep(2000, 4)
                        time.sleep(5)
                        limpaTela()
                limpaTela()
                
                quantidade = int(input("Quantas # tinham?\n> "))
            
                if quantidade == valorAleatorio:
                    if escolha == 1:
                        pontuacao += 20
                    elif escolha == 2:
                        pontuacao += 50
                    elif escolha == 3:
                        pontuacao += 100
                        
                    print("Você acertou! Paranabéns!!!")
                    break
                else:
                    if escolha == 1:
                        pontuacao -= 10
                    elif escolha == 2:
                        pontuacao -= 20
                    elif escolha == 3:
                        pontuacao -= 30
    
                    if pontuacao < 0: pontuacao = 0
                        
                    print("Você errou :,(")
                    break
            if input(f"Pontuação atual: {pontuacao}\nQuer tentar novamente? (S/n)\n> ")[0].lower() == 'n':
                break
            
        if pontuacao > recorde:
            recorde = pontuacao
            #Exibe o recorde da nova pontuação do jogador
            print(f"NOVO RECORDE: {pontuacao}")
            if input("Deseja subscrever o recorde? (S/n)\n> ")[0].lower() == 's':
                while True:
                    nome = input("Insira seu nome: ")
                    if len(nome) > 0 and len(nome) <= 15:
                        break
                    else: #Nome só será sobescrito se o nome possuir ao menos 1 e até 15 caracteres
                        print("Insira um nome entre 1 a 15 caracteres!")
                frase = nome + ": " + str(pontuacao)
                arquivo = open("pontuacao.txt", 'w')
                arquivo.write(frase)
                arquivo.close()        
    elif escolha == 2: # Opção 2 = Recorde
        limpaTela()
        with open("pontuacao.txt") as arquivo:
            for linha in arquivo:
                print(f"======================================\nRecorde: {linha}\n=========================================")
    elif escolha == 3: # Opção 3 = Saída
        break
    
    print("Obrigado por jogar! :)")
    time.sleep(1)