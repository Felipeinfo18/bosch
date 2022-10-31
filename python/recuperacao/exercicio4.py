# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:09:26 2022

@author: disrct
"""

def notas(*args, sit=False):
    if sit:
        sit = ""
        media = sum(args) / len(args)
        if media >= 7:
            sit = "Boa"
        elif 5 <= media < 7:
            sit = "Razoável"
        elif media < 5:
            sit = "Ruim"
            
        return {'total': len(args), 'maior': max(args), 'menor': min(args), 'média': round(media, 2), 'situação': sit}   
    return len(args), max(args), min(args), sum(args) / len(args)
        
    
print(notas(5.5, 2.5, 9.9, sit=True))
