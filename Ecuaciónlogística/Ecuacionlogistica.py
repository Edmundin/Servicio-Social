# Comenzaremos obteniendo los datos para la progresión logística

# x_{t+1} = Rx_t(1-x_t), donde 0 <= x_0 <= 1

# Importamos las liberias necesarias

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


@cache #Guárdará los datos para intentar acelarar el proceso (es un decorador)
def logistic (R, x0, N):
    x = x0
    x_list = [x0]
    for i in range(N-1):
        x = R * x * (1.0 - x)
        x_list.append(x)

    return x_list, R, x0

def graficar(x_list, R, x0):
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(16, 6), facecolor='lightgray')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Valor de x')
    plt.title(f'\nEcuación logística\n\nR={R}  |  x0={x0}\n')
    plt.plot(x_list, 'o:r')
    plt.show()


#Jugar con los datos

#e1, R, x0 = logistic(2, 0.99, 31)
#graficar(e1, R, x0)

#el_1 = logistic(2, 0.99, 31)
#el_1 = pd.DataFrame(el_1)


#el_2 = logistic(3.1, 0.85, 91)
#el_2 = pd.DataFrame(el_2)

#el_4 = logistic(3.84, 0.67, 101)
#el_4 = pd.DataFrame(el_4)

# Guardar series de tiempo
#el_1.to_csv('el_1.csv')
#el_2.to_csv('el_2.csv')
#el_4.to_csv('el_4.csv')


#for elems in valor_r:
#     print(elems)
#     log = 0
#     log = reglog_iteracion(randint(100, N), Xo, elems)
#     valor_f.append(log)
#     eje_r.append(elems)

#plt.scatter(eje_r, valor_f)
#plt.show()

# Guardar datos en CsV
