# -*- coding: utf-8 -*-
"""MatrizDeterminateNumPy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fnkgjqdMBFYhPmTUdPq0eGOpt350VbLe

Matriz e determinante por Numpy
"""

import numpy as np

matriz = np.random.randint(1,11,(3,3))

print(matriz)

determine = np.linalg.det(matriz)

print("Determinante da matriz:", determine)