# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:40:01 2022

@author: DISRCT
"""

from random import sample

tuple = tuple(sample(range(0, 10), 5))
print(tuple)

print(f"O menor valor é {min(tuple)}")
print(f"O maior valor é {max(tuple)}")
count = 0

for i in tuple:
    if 5 == i:
        count += 1
        
print(f"O número 5 aparece {count} vezes")


if 2 in tuple:
    print(f"O primeiro número 2 aparece na posição {tuple.index(2)}")
else:
    print("O número 2 não existe na tupla")