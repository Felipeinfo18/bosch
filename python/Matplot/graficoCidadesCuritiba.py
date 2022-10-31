# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:57:51 2022

@author: disrct
"""

import numpy as np
import matplotlib.pyplot as plt

labels = ["Lapa", "Itaperuçu", "Rio Negro", "Tijucas do Sul", "Tunas do Paraná"]
val = [1157893, 416764, 858233, 362860, 88324]

cidades = np.array(labels)
habitantes = np.array(val)

for i in range(len(val)):
    val[i] = str(val[i])

p, tx, autotexts = plt.pie(val, labels=cidades, 
        autopct="", shadow=True)


plt.rcParams["figure.figsize"] = (30, 38)
plt.rcParams.update({'font.size': 45})

for i, a in enumerate(autotexts):
    a.set_text("{} hab.".format(habitantes[i]))
    