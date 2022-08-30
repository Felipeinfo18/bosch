# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:23:37 2022

@author: DISRCT
"""
import math

class Calculadora:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def soma(self, num1, num2):
        return num1 + num2
    
    def subtrai(self, num1, num2):
        return num1 - num2
            
    def multiplica(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2
            
        
class CalculadoraCientifica(Calculadora):
    def __init__(self):
        pass
    
    def quadrado(self, num):
        return math.pow(num, 2) 
    def raiz(self, num):
        return math.sqrt(num) 
    def log10(self, num):
        return math.log10(num) 
    def fatorial(self, num):
        return math.factorial(num) 
   
calcula = CalculadoraCientifica()
print(calcula.quadrado(5))