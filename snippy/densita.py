import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Misure dirette dei diametri e delle masse per le sfere (mettete i vostri numeri).
# Potete anche leggere i dati da file, usando np.loadtxt(), se lo trovate comodo.
m = np.array([24.769, 11.887, 8.374, 3.528])
sigma_m = np.full(m.shape, 0.001)
d = np.array([18.25, 14.28, 12.69, 9.52])
sigma_d = np.full(d.shape, 0.01)
# Calcolo del volume (notate la propagazione dell'errore su V!)
r = d / 2.0
sigma_r = sigma_d / 2.0
V = 4.0 / 3.0 * np.pi * r**3.0
sigma_V = V * 3.0 * sigma_d / d

def line(x, a, b):
    """Modello lineare di fit.
    """
    return a * x + b

def power_law(x, norm, index):
    """Modello di tipo legge di potenza.
    """
    return norm * (x**index)

plt.figure('Grafico massa-volume')
plt.errorbar(m, V, sigma_V, sigma_m, fmt='o')
popt, pcov = curve_fit(line, m, V)
a_hat, b_hat = popt
sigma_a, sigma_b = np.sqrt(pcov.diagonal())
# Attenzione alle cifre significative quando 
# si riportano questi valori sulla relazione:
print(f'a = {ahat} +/- {sigma_ahat}')
print(f'b = {bhat} +/- {sigma_bhat}')
# Grafico del modello di best fit.
x = np.linspace(0., 4000., 100)
plt.plot(x, line(x, a_hat, b_hat))
plt.ylabel('Volume [mm$^3$]')
plt.xlabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_volume.pdf')

plt.figure('Grafico massa-raggio')
plt.errorbar(r, m, sigma_m, sigma_r, fmt='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Raggio [mm]')
plt.ylabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_raggio.pdf')

plt.show()
