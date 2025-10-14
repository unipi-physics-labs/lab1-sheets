import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Dati---mettete le vostre misure!
# Qui potete anche leggere i dati da file, usando il metodo np.loadtxt(),
# se lo trovate comodo.
d = np.array([0.100, 0.200, 0.300, 0.400])
sigma_d = np.full(d.shape, 0.002)
T = np.array([1.943, 1.570, 1.518, 1.572])
sigma_T = np.array([0.005, 0.004, 0.006, 0.005])

# Definizione dell'accelerazione di gravita`.
g = 9.81

def period_model(d, l):
    """Modello per il periodo del pendolo.
    """
    return 2.0 * np.pi * np.sqrt((l**2.0 / 12.0 + d**2.0) / (g * d))

plt.figure('Periodo')
# Scatter plot dei dati.
plt.errorbar(d, T, sigma_T, sigma_d, fmt='o')
# Fit---notate che questo e` un fit ad un solo parametro.
popt, pcov = curve_fit(period_model, d, T, sigma=sigma_T)
l_hat = popt[0]
sigma_l = np.sqrt(pcov[0, 0])
# Confrontate i parametri di best fit con la vostra misura diretta!
print(l_hat, sigma_l)
# Grafico del modello di best-fit.
x = np.linspace(0.05, 0.5, 100)
plt.plot(x, period_model(x, l_hat))
plt.xlabel('d [m]')
plt.ylabel('Periodo [s]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_raggio.pdf')

plt.show()
