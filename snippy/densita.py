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

def line(x, m, q):
    """Modello lineare di fit.
    """
    return m * x + q

def power_law(x, norm, index):
    """Modello di tipo legge di potenza.
    """
    return norm * (x**index)

plt.figure('Grafico massa-volume')
plt.errorbar(V, m, sigma_m, sigma_V, fmt='o')
popt, pcov = curve_fit(line, V, m)
m_hat, q_hat = popt
sigma_m, sigma_q = np.sqrt(pcov.diagonal())
print(m_hat, sigma_m, q_hat, sigma_q)
# Grafico del modello di best fit.
x = np.linspace(0., 4000., 100)
plt.plot(x, line(x, m_hat, q_hat))
plt.xlabel('Volume [mm$^3$]')
plt.ylabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_volume.pdf')

plt.figure('Grafico massa-raggio')
plt.errorbar(r, m, sigma_m, sigma_r, fmt='o')
popt, pcov = curve_fit(power_law, r, m)
norm_hat, index_hat = popt
sigma_norm, sigma_index = np.sqrt(pcov.diagonal())
print(norm_hat, sigma_norm, index_hat, sigma_index)
x = np.linspace(4., 10., 100)
plt.plot(x, power_law(x, norm_hat, index_hat))
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Raggio [mm]')
plt.ylabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_raggio.pdf')

plt.show()
