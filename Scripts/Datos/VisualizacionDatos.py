import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#os.chdir('C:/Users/aedmu/Desktop/Proyectos/Servicio_social/Datos')

#num = int(input())
ticket, fecha = input().split()

df = pd.read_csv('C:/Users/aedmu/Desktop/Proyectos/Servicio_social/Datos/Info/{t}/{t}_{f}.csv'.format(t=ticket,f=fecha), header = 1)

serietiempo = df["Open"]
#df.to_csv(nombre, index=False)

serietiempo = np.array(serietiempo)
print(serietiempo)
mini = serietiempo.min()
maxi = serietiempo.max()
std = serietiempo.std()
prom = serietiempo.mean()
difabs = maxi-mini
minind = np.argmin(serietiempo)
maxind = np.argmax(serietiempo)

textstr = '\n'.join((
    r'$\mathrm{min}=%.2f$' % (mini, ),
    r'$\mathrm{max}=%.2f$' % (maxi, ),
    r'dif abs=%.2f' % (difabs, ),
    r'$\mathrm{prom}=%.2f$' % (prom, ),
    r'$\sigma=%.2f$' % (std, )))

plt.rcParams["figure.figsize"] = (15,7)
fig, ax = plt.subplots()
plt.plot(serietiempo)
plt.scatter([minind,maxind],[mini,maxi],c="r")
plt.title("IPC_"+fecha,fontsize=20)
plt.ylabel("IPC", fontsize=15)
plt.xlabel("Hora", fontsize=17)


medihora = int(len(hora)/30)
lhoras =[hora[0]]
xlhoras=[0]
for i in range(medihora):
    lhoras.append(hora[30*(i+1)])
    xlhoras.append(30*(i+1))

ax.set_xticks(xlhoras)
ax.set_xticklabels(lhoras)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.37)
ax.text(1.005, 0.99, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.savefig("{t}_".format(t = ticket )+fecha+'.png',dpi=200)
plt.show()
plt.close()
