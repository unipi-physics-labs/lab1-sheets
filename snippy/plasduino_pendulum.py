# Programma di esempio per l'analisi del file prodotto dal modulo pendulum  di plasduino
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.ion() # interactive on

# Lettura del file di dati in ingresso (da modificare con il percorso al vostro file in ingresso).
ii, edge, tt = scipy.loadtxt('data/pendulum.txt', unpack = True)

# Calcolo dei tempi di transito Tr e del periodo T calcolato come la differenza tra
# il tempo di ingresso della bandierina e il tempo al passaggio successivo che completa 1 periodo
t  = []; T = []; Tr = [];
for i in range(3, len(tt)-1, 4):
    t.append(0.5*(tt[i]+tt[i-1]))
    Tr.append(tt[i] - tt[i-1])    # diff. tra uscita e ingresso della bandierina
    T.append((tt[i+1] - tt[i-3])) # si puo' calcolare in altri modi?
t  = np.array(t); T  = np.array(T); Tr = np.array(Tr)

# Definizione della geometria del pendolo [cm] (da modificare con le vostre misure).
w = 2.05; l = 113.5; d = 116.5
# Calcolo di velocita' e angolo
v = (w/Tr)*(l/d)
Theta = np.arccos(1. - (v**2)/(2*981.*l))

# Funzioni di fit per velocita' e angolo
def f_v(x, v0, tau):
    return v0*np.exp(-x/tau)

def f_Theta(x, p1, p2):
    return 2*np.pi*np.sqrt(l/981.)*(1 +p1*(x**2) +p2*(x**4))

# Fit di V vs t
popt_v, pcov_v = curve_fit(f_v, t, v, np.array([500., 100.]))
v0_fit,   tau_fit = popt_v
dv0_fit, dtau_fit = np.sqrt(pcov_v.diagonal())
print('v0  = %.2f +- %.2f cm/s' % (v0_fit,  dv0_fit))
print('tau = %.2f +- %.2f s' % (tau_fit, dtau_fit))
# Plot di V vs t
plt.figure(1)
plt.xlabel('Tempo [s]'); plt.ylabel('v [cm/s]'); plt.grid(color = 'gray')
plt.plot(t, v, '+', t, f_v(t, v0_fit, tau_fit))
plt.savefig('pendolo_VvsT.png')
# Plot di T vs Theta e dei residui rispetto alla funzione attesa
plt.figure(2)
plt.subplot(211)
plt.ylabel('Periodo [s]') 
plt.plot(Theta, T, 'o', Theta, f_Theta(Theta, 1./16, 11./3072), 'r')
plt.subplot(212)
plt.xlabel('Angolo [rad]'); plt.ylabel('Periodo data - modello [ms]') 
plt.plot(Theta, 1000*(T-f_Theta(Theta, 1./16, 11./3072)))
plt.savefig('pendolo_TvsTheta.png')

