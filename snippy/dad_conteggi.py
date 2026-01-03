import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import scipy

def p_value(chisq, ndof):
    p = scipy.stats.chi2.cdf(chisq, ndof)
    # If the probability is > 50% , take the complement.
    if p > 0.5:
        p = 1.0 - p
    return p

# ogni entry dell'array l contiene il numero di entrate in un minuto, la lughezza dell'array corrisponde quindi al tempo totale di osservazione in minuti:
#l = np.array([ ... ])

# Calcolo della statistica del campione delle lunghezze dei versi, utilizzando le
# funzioni appropriate di numpy.
N = len(l)
m = l.mean()
s = l.std(ddof=1)
print(f"Numero di osservazioni: {N}")
print(f"Media: {m}")
print(f"Deviazione standard: {s}")

# Definizione dei canali dell'istogramma---attenzione ad avere esattamente un valore
# intero all'interno di ogni bin! I -0.5 e +1.5 servono per far apparire le barre al
# centro dei canali. Stampare per credere.
binning = np.arange(l.min() - 0.5, l.max() + 1.5)

# Creazione dell'istogramma. La funzione hist() di matplotlib restituisce tre variabili,
# ma a noi interessa solo la prima, ovvero il contenuto dei canali dell'istogtramma.
plt.figure('Lunghezza dei versi')
o, _, _ = plt.hist(l, bins=binning, rwidth=0.25, label='Conteggi')
plt.xlabel('# entrate/minuto')
plt.ylabel('Occorrenze')

# Calcolo dei valori attesi nel modello Poissoniano. Verificate che la
# definizione di k alla riga qui sotto corrisponde a tutti i valori interi compresi tra
# la minima e la massima lunghezza dei versi. 
k = np.arange(l.min(), l.max() + 1)
e_poisson = N * poisson.pmf(k, m)

# Gia` che ci siamo, disegnamo i valori attesi sull'istogramma di partenza.
# Notate che disegnamo la distribuzione di Poisson di best fit come un grafico a barre
# (spostato rigidamente di 0.3 unita` sulla sinistra per far si` che non si sovrapponga
# all'istogramma di partenza).
plt.bar(k - 0.3, e_poisson, width=0.25, color='#ff7f0e', label='Poisson')

# Calcolo del chi quadro nelle due ipotesi. Assicuratevi di capire esattamente perche'
# le due righe seguenti corrispondono all'espressione che abbiamo studiato.
chi2_poisson = ((o - e_poisson)**2. / e_poisson).sum()
dof_poisson = len(k) - 1 - 1
print(f'chi2 per la Poissoniana: {chi2_poisson} / {dof_poisson} dof')

plt.legend()
plt.show()
