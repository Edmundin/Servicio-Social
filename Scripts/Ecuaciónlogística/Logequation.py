import math
import statistics
import numpy as np # Paquete científico de python
import matplotlib.pyplot as plt # Dataviz
from random import randint # Función para generar números aleatorios
import pandas as pd # Paquete que nos permite manipular vectores
                    # matemáticos
import seaborn as sns
from functools import cache
import plotly.figure_factory as ff
import plotly.express as px
from collections import Counter
import numpy as np

R_list = np.linspace(2.0, 4.0, 1000)
x0 = 0.6
N = 500

def logis(r):
    x_list = [x0]
    for i in range(N-1):
        x_list.append(r * x_list[-1] * (1 - x_list[-1]))
    return x_list[400:]

x_select = []
R_select = []
for r in R_list:
    x_select.append(logis(r))
    R_select.append([r] * 100)

x_select = np.array(x_select).ravel()
R_select = np.array(R_select).ravel()

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(16, 6), facecolor='lightgray')
plt.xlabel('El valor de R')
plt.ylabel('El valor de x')
plt.title(f'\nEl diagrama de bifurcación \n\n2.0 < R < 4.0  |  x0=0.3\n')
plt.scatter(R_select, x_select, color='red', s=0.1)
#plt.savefig('bifurcation_diagram.png')
plt.show()
