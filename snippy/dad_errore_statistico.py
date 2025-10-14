import numpy as np
from matplotlib import pyplot as plt

# Leggiamo le misure da un file di testo che avrete preventivamente
# riempito durante l'esecuzione delle misure. Assumiamo che il file abbia una
# sola colonna con il tempo totale corrispondente a 10 periodi, con un
# valore per riga.
file_path = 'data/pendolo.txt'
T = np.loadtxt(file_path)
# Dividiamo per 10 tutte le misure, per passare alla stima del singolo periodo.
T /= 10

# Calcoliamo media e deviazione standard della media utilizzando le funzioni di
# numpy:
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std
# In particolare il ddof=1 serve per avere il termine (N - 1) al denominatore.
m = np.average(T)
s = np.std(T, ddof=1)
# Dobbiamo dividere per la radice del numero di misure per passare
# dalla deviazione standard del campione a quella della media.
sm = s / np.sqrt(len(T))
print(f'Periodo: {m} +/- {sm}')

# Calcolo della media e deviazione standard sui campioni parziali.
# Potete cambiare i due 5 a vostro piacimento.
N_sub = np.arange(5, len(T), 5)
m_sub = []
s_sub = []
sm_sub = []
for n in N_sub:
    # Ricordate lo slicing di array di numpy:
    # https://numpy.org/doc/stable/reference/arrays.indexing.html
    t = T[:n]
    m = np.average(t)
    s = np.std(t, ddof=1)
    sm = s / np.sqrt(n)
    m_sub.append(m)
    s_sub.append(s)
    sm_sub.append(sm)

plt.figure('Valore centrale')
plt.errorbar(N_sub, m_sub, sm_sub, fmt='o')
plt.xlabel('Numero di misure')
plt.ylabel('Stima del periodo [s]')

plt.figure('Incertezza')
plt.errorbar(N_sub, s_sub, fmt='o', label='$s$')
plt.errorbar(N_sub, sm_sub, fmt='o', label='$s_m$')
plt.xlabel('Numero di misure')
plt.ylabel('Incertezza [s]')
plt.legend()
# Possiamo provare a mostrare lo scaling previsto con 1/sqrt(N)
x = np.linspace(5, len(T), 200)
y = s / np.sqrt(x)
plt.plot(x, y, ls='dashed')

plt.show()
