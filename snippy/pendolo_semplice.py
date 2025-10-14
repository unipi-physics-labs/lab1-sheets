import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Misure del periodo di oscillazione in funzione della lunghezza.
l = np.array([440., 530., 615., 680., 775.])
sigma_l = np.array([1.] * len(l))
T = np.array([1.328, 1.449, 1.565, 1.649, 1.770])
sigma_T = np.array([0.006, 0.006, 0.002, 0.002, 0.006])

def power_law(x, norm, index):
    """Funzione di fit (una legge di potenza).
    """
    return norm * (x**index)

plt.figure('Grafico periodo-lunghezza')
plt.errorbar(l, T, sigma_T, sigma_l, fmt='o')
# Il fit in dettaglio: questa e` la funzione che esegue il fit e restituisce i parametri di best-fit e
# tutto quello che serve (la cosiddetta matrice di covarianza) per stimare gli errori associati. Per il
# momento non passiamo le incertezze di misura al fit (per un motivo che vedremo piu` avanti) ma
# ricordate che in generale questo non e` corretto.
popt, pcov = curve_fit(power_law, l, T)
# Spacchettiamo l'array dei parametri per averli disponibili separatamente
norm_fit, index_fit = popt
# Calcoliamo le incertezze di misura (a questo livello l'unica cosa che dovete sapere e` che sono la
# radice quadrata degli elementi diagonali della matrice di covarianza).
sigma_norm_fit, sigma_index_fit = np.sqrt(pcov.diagonal())
# Facciamo stampare i parametri (per la relazione non dimenticate di convertire nelle unita` di misura
# opportune e di scrivere il numero corretto di cifre significative)
print(norm_fit, sigma_norm_fit, index_fit, sigma_index_fit)
# Infine: facciamo il grafico del modello di best fit.
x = np.linspace(200., 1000., 100)
plt.plot(x, power_law(x, norm_fit, index_fit))
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Lunghezza [mm]')
plt.ylabel('Periodo [s]')
plt.grid(ls='dashed', which='both')

# Misure del periodo di oscillazione in funzione dell'ampiezza.
theta0 = np.array([3.7, 7.4, 11.2, 18.8, 26.9])
sigma_theta0 = np.array([0.1] * len(theta0))
T = np.array([1.752, 1.759, 1.767, 1.772, 1.786])
sigma_T = np.array([0.005, 0.004, 0.007, 0.009, 0.005])

plt.figure('Grafico periodo-ampiezza')
plt.errorbar(theta0, T, sigma_T, sigma_theta0, fmt='o')
# Disegnamo il modello, assumendo un valore ragionevole per T0.
T0 = 1.757
x = np.linspace(0., 30., 100)
# Notate la conversione da gradi a radianti!
y = T0 * (1. + np.radians(x)**2. / 16.)
plt.plot(x, y)
plt.xlabel('Ampiezza di oscillazione [$^\\circ$]')
plt.ylabel('Periodo [s]')
plt.grid(ls='dashed', which='both')

plt.show()
