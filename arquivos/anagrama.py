# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:04:45 2022

@author: disrct
"""
import random

#Função que abre o arquivo txt e devolve uma lista com seu conteúdo
def pegaPalavras():
    with open('anagrama.txt') as texto:
        for linha in texto:
            if linha != '\n': 
                palavra = linha.split(" ")
                palavra = palavra[0].strip().lower()
                palavras.append(palavra)
    return palavras

#Função que abre o arquivo txt de dicas e retorna uma dica aleatória
def pegaDicaAleatoria():
    dicas = []
    with open('dicas.txt') as texto:
        for linha in texto:
            if linha != '\n': 
                dicas.append(linha.strip())
    
    return dicas[random.randint(0, len(dicas)-1)]
    
#Função que filtra a lista de palavras de acordo com a dificuldade escolhidade e a retorna
def filtraDificuldade(palavras, dificuldade):
    palavrasDificuldade = []
    
    for i in palavras:
        if dificuldade == 1:
            if len(i) == 4:
                palavrasDificuldade.append(i)
        elif dificuldade == 2:
            if len(i) == 6 :
                palavrasDificuldade.append(i)
            
        elif dificuldade == 3:
            if len(i) == 9:
                palavrasDificuldade.append(i)             
    return palavrasDificuldade

#Função que verifica se o usuário acertou ou não a palavra aleatória
def verificaPalavra(palavra, palavraAleatoria):
    global pontos
    if palavraAleatoria == palavra: 
        print("Você acertou! Parabéns\n")
        return True
    else: 
        print("Você errou -20 pontos!\n")
        pontos -= 20
        if pontos == 0:
            print(f"Você perdeu! A palavra era: {palavraAleatoria}\n")
            return True

#Função que embaralha palavras
def embaralhaPalavra(palavraAleatoria):
    palavraEmbaralhada = ""           
    listaNumeros = []            
    
    for i in range(len(palavraAleatoria)):
        while True:
            num = random.randint(0, len(palavraAleatoria)-1)
            if listaNumeros.count(num) == 0: 
                listaNumeros.append(num)
                break
    
    
    for i in listaNumeros:
        palavraEmbaralhada += palavraAleatoria[i]
    
    return palavraEmbaralhada
     
#Erro para verificar apenas valores entre as opções do menu (1 a 3)   
class ValorIncorreto(Exception):
    print("Digite um número entre 1 e 3")

#Início do jogo
while True:
    pontos = 100
    acertou = False
    palavras = []
    
    verifica = True
    
    while verifica:
        verifica = False
        try:
            print("""
                     ====================================
                     [1] - Fácil
                      [2] - Intermediário
                       [3] - Difícil ( Modo GAMER )
                       ===================================""")
    
            dificuldade = int(input("Escolha um nivel de dificuldade: "))
            
            if dificuldade <= 0 or dificuldade > 3: raise ValorIncorreto 
        except ValueError:
            verifica = True
            print("Valor inválido! Tente novamente")
        except ValorIncorreto:
            verifica = True
            print("Valor inválido! Tente novamente")
            
    palavras = pegaPalavras()
    
    palavrasDificuldade = filtraDificuldade(palavras, dificuldade)
    
    palavraAleatoria = palavrasDificuldade[random.randint(0, len(palavrasDificuldade)-1)]
 
    #Embaralha a palavra até que ela seja diferente da palavra original
    while True:
        palavraEmbaralhada = embaralhaPalavra(palavraAleatoria)
        if palavraEmbaralhada != palavraAleatoria:
            break
    
    while True:
        print(f"\n==============================================\nPontuação: {pontos}\nPalavra Embaralhada: {palavraEmbaralhada}\nPedir dica (1)\n==============================================\n")
        
        while True:
            palavra = input("Tente advinhar a palavra: ")
            if palavra != "": break
        if palavra.isdigit():
            if int(palavra) == 1:
                dica = pegaDicaAleatoria()
                print(dica)
        elif verificaPalavra(palavra, palavraAleatoria): break
           
    decisao = ""
    
    while True:
        try:
            decisao = input("Deseja jogar novamente? (S/n): ")
               
            if decisao[0].lower() == 'n' or decisao[0].lower() == 's':
                break
        except Exception:
            print("Valor inválido! Tente novamente!")
        
    #Condição para sair do jogo
    if decisao[0].lower() == 'n':
        break