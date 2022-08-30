# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:14:49 2022

@author: DISRCT
"""

class Carro():
    def __init__(self, marca: str, cor: str, dono: str, ano: int):
        self.__marca = marca
        self.__cor = cor
        self.__dono = dono
        self.__ano = ano
        Carro.GPS = True
        
    @staticmethod
    def LigarGPS():
        Carro.GPS = True
    
    @staticmethod
    def DesligarGPS():
        Carro.GPS = False
    
    def MostrarAtributos(self):
        print(f"O {self.__marca} {self.__cor} da {self.__dono} do ano {self.__ano} esta com o GPS ", end="")
        
        try:
            if Carro.GPS:
                print("Ligado\n")
            else:
                print("Desligado\n")
        except Exception:
            print("Erro: GPS não existe")
            pass

carrosBosch = []

for i in range(40):
    carrosBosch.append(Carro("Honda Civic", "Prata", "Bosch", 2022))

for i in range(40):
    carrosBosch[i].MostrarAtributos()
    