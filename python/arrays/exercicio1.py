# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:04:32 2022

@author: DISRCT
"""

import numpy as np

array = np.arange(20, 91)

array = array[array%2==0]
print(array)