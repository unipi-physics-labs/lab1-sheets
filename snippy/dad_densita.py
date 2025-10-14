import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Misure dirette (queste sono ovviamente inventate). Sostituite con le vostre o,
# ancora meglio, leggete da un file.
d = 12.3 # Diametro interno del cilindro in cm
sigma_d = 0.1 # Errore sul diametro.
h = np.array([2.3, 4.2, 6.1])
sigma_h = np.full(h.shape, 0.1)
m = np.array([274., 498., 727.])
sigma_m = np.full(m.shape, 5.)

# Calcolo del volume e propagazione degli errori. Notate che, a questo punto, le
# misure di volume non sono piu` indipendenti tra di loro. Sapreste spiegare il
# perche'?
V = np.pi / 4. * d**2. * h
sigma_V = V * np.sqrt(4. * (sigma_d / d)**2. + (sigma_h / h)**2.)

# Definizione della funzione di fit.
def line(x, m, q):
    return m * x + q

# Scatter plot delle misure, con le incertezze associate.
plt.figure('Grafico massa-volume')
plt.errorbar(V, m, sigma_m, sigma_V, fmt='o')
plt.xlabel('Volume [cm$^3$]')
plt.ylabel('Massa [g]')
plt.grid(ls='dashed')

# Il fit in dettaglio: questa e` la funzione che esegue il fit e restituisce i
# parametri di best-fit e tutto quello che serve (la cosiddetta matrice di
# covarianza) per stimare gli errori associati.
# Per il momento non passiamo le incertezze di misura al fit (per un motivo che
# vedremo piu` avanti) ma ricordate che in generale questo non e` corretto.
popt, pcov = curve_fit(line, V, m)
# Spacchettiamo l'array dei parametri per averli disponibili separatamente
mhat, qhat = popt
# Calcoliamo le incertezze di misura (a questo livello l'unica cosa che dovete
# sapere e` che sono la radice quadrata degli elementi diagonali della matrice
# di covarianza).
sigma_mhat, sigma_qhat = np.sqrt(pcov.diagonal())
# Facciamo stampare i parametri (per la relazione non dimenticate di convertire
# nelle unita` di misura opportune, ove necessario, e di scrivere il numero
# corretto di cifre significative).
print(f'm = {mhat} +/- {sigma_mhat}')
print(f'q = {qhat} +/- {sigma_qhat}')

# Infine: facciamo il grafico del modello di best fit.
x = np.linspace(0., 1000, 100)
plt.plot(x, line(x, mhat, qhat))

plt.show()
