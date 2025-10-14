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
# caso A, preso da fillDataTablePlain
t_A  = []; T_A = []; Tr_A = [];
for i in range(3, len(tt)-1, 2):
    t_A.append(0.5*(tt[i]+tt[i-1]))
    Tr_A.append(tt[i] - tt[i-1])    # diff. tra uscita e ingresso della bandierina
    T_A.append((tt[i+1] - tt[i-3])) # si puo' calcolare in altri modi?
t_A  = np.array(t_A); T_A  = np.array(T_A); Tr_A = np.array(Tr_A)

# caso B, proposto da Francesco
t_B  = []; T_B = []; Tr_B = [];
for i in range(5, len(tt)-1, 4):
    t_B.append(0.5*(tt[i+2]-tt[i+1]))
    Tr_B.append(tt[i+2]-tt[i+1])
    #T_B.append((tt[i+0]-tt[i-4]))
    #T_B.append((tt[i+1]-tt[i-3]))
    T_B.append((tt[i+2]-tt[i-2]))
    #T_B.append((tt[i+3]-tt[i-1]))
t_B  = np.array(t_B); T_B  = np.array(T_B); Tr_B = np.array(Tr_B)

# caso C, preso da fillDataTableAdvanced
t_C  = []; T_C = []; Tr_C = [];
for i in range(5, len(tt)-3, 2):
    t1 = 0.5*(tt[i-4] + tt[i-5])
    t2 = 0.5*(tt[i-2] + tt[i-3])
    t3 = 0.5*(tt[i  ] + tt[i-1])
    t4 = 0.5*(tt[i+2] + tt[i+1])
    dt2 = tt[i-2] - tt[i-3]
    dt3 = tt[i] - tt[i-1]
    t_C.append(0.5*(t2 + t3))
    Tr_C.append(0.5*(dt2 + dt3))
    T_C.append(0.5*(t3 - t1 + t4 - t2))
t_C  = np.array(t_C); T_C  = np.array(T_C); Tr_C = np.array(Tr_C)


# Definizione della geometria del pendolo [cm] (da modificare con le vostre misure).
w = 2.05; l = 113.5; d = 116.5
# Calcolo di velocita' e angolo
v_A = (w/Tr_A)*(l/d)
Theta_A = np.arccos(1. - (v_A**2)/(2*981.*l))

v_B = (w/Tr_B)*(l/d)
Theta_B = np.arccos(1. - (v_B**2)/(2*981.*l))

v_C = (w/Tr_C)*(l/d)
Theta_C = np.arccos(1. - (v_C**2)/(2*981.*l))

# Funzioni di fit per velocita' e angolo
def f_Theta(x, p1, p2):
    return 2*np.pi*np.sqrt(l/981.)*(1 +p1*(x**2) +p2*(x**4))


# Plot di T vs Theta e dei residui rispetto alla funzione attesa
plt.figure(2)
plt.subplot(211)
plt.ylabel('Periodo [s]'); plt.grid(color = 'gray')
plt.plot(Theta_A, T_A, 'o', label = 'caso A')
plt.plot(Theta_B, T_B, 'o', label = 'caso B')
plt.plot(Theta_A, f_Theta(Theta_A, 1./16, 11./3072), 'r', )
plt.plot(Theta_B, f_Theta(Theta_B, 1./16, 11./3072), 'r')
#plt.plot(Theta_C, T_C, 'o', label = 'caso C')
#plt.plot(Theta_C, f_Theta(Theta_C, 1./16, 11./3072), 'r')
plt.legend(loc=2)
plt.subplot(212)
plt.xlabel('Angolo [rad]'); plt.ylabel('Periodo data - modello [ms]'); plt.grid(color = 'gray')
plt.plot(Theta_A, 1000*(T_A-f_Theta(Theta_A, 1./16, 11./3072)), label = 'caso A')
plt.plot(Theta_B, 1000*(T_B-f_Theta(Theta_B, 1./16, 11./3072)), label = 'caso B')
#plt.plot(Theta_C, 1000*(T_C-f_Theta(Theta_C, 1./16, 11./3072)), label = 'caso C')
plt.legend(loc=2)
plt.savefig('pendolo_TvsTheta_TestT.png')

