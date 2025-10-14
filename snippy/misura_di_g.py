import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Misura di allungamento e periodo di oscillazione in funzione della massa appesa.
m = np.array([5.005, 10.006, 20.011, 50.032])
sigma_m = np.array([0.001] * len(m))
l = np.array([152., 171., 220., 351.])
sigma_l = np.array([1.] * len(l))
T = np.array([0.530, 0.611, 0.739, 1.044])
sigma_T = np.array([0.005, 0.005, 0.006, 0.004])
# Calculate the square of the period and propagate the errors.
T2 = T**2.
sigma_T2 = 2 * T * sigma_T

def line(x, m, q):
    """Funzione di fit (una semplice retta).
    """
    return m * x + q

plt.figure('Grafico allungamento-massa')
plt.errorbar(m, l, sigma_l, sigma_m, fmt='o')
# Il fit in dettaglio: questa e` la funzione che esegue il fit e restituisce i parametri di best-fit e
# tutto quello che serve (la cosiddetta matrice di covarianza) per stimare gli errori associati. Per il
# momento non passiamo le incertezze di misura al fit (per un motivo che vedremo piu` avanti) ma
# ricordate che in generale questo non e` corretto.
popt, pcov = curve_fit(line, m, l)
# Spacchettiamo l'array dei parametri per averli disponibili separatamente
m_fit, q_fit = popt
# Calcoliamo le incertezze di misura (a questo livello l'unica cosa che dovete sapere e` che sono la
# radice quadrata degli elementi diagonali della matrice di covarianza).
sigma_m_fit, sigma_q_fit = np.sqrt(pcov.diagonal())
# Facciamo stampare i parametri (per la relazione non dimenticate di convertire nelle unita` di misura
# opportune e di scrivere il numero corretto di cifre significative)
print(m_fit, sigma_m_fit, q_fit, sigma_q_fit)
# Infine: facciamo il grafico del modello di best fit.
x = np.linspace(0., 60., 100)
plt.plot(x, line(x, m_fit, q_fit))
plt.xlabel('Massa [g]')
plt.ylabel('Allungamento [mm]')
plt.grid(ls='dashed')

plt.figure('Grafico periodo quadro-massa')
plt.errorbar(m, T2, sigma_T2, sigma_m, fmt='o')
popt, pcov = curve_fit(line, m, T2)
m_fit, q_fit = popt
sigma_m_fit, sigma_q_fit = np.sqrt(pcov.diagonal())
print(m_fit, sigma_m_fit, q_fit, sigma_q_fit)
x = np.linspace(0., 60., 100)
plt.plot(x, line(x, m_fit, q_fit))
plt.xlabel('Massa [g]')
plt.ylabel('Periodo al quadrato [s$^2$]')
plt.grid(ls='dashed')

plt.show()
