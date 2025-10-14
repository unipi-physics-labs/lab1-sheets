import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, binom

# Array con la lunghezza dei versi---potete definirlo a mano nello script
# oppure leggerlo da file.
l = ...

# Calcolo della statistica del campione delle lunghezze dei versi, utilizzando le
# funzioni appropriate di numpy.
N = len(l)
m = l.mean()
s = l.std(ddof=1)
print(f'Numero di versi: {N}')
print(f'Lunghezza media dei varsi: {m}')
print(f'Deviazione standard delle lunghezze: {s}')

# Definizione dei canali dell'istogramma---attenzione ad avere esattamente un valore
# itntero all'interno di ogni bin! I -0.5 e +1.5 servono per far apparire le barre al
# centro dei canali. Stampare per credere.
binning = np.arange(l.min() - 0.5, l.max() + 1.5)

# Creazione dell'istogramma. La funzione hist() di matplotlib restituisce tre variabili,
# ma a noi interessa solo la prima, ovvero il contenuto dei canali dell'istogtramma.
plt.figure('Lunghezza dei versi')
o, _, _ = plt.hist(l, bins=binning, rwidth=0.25, label='Conteggi')
plt.xlabel('Numero di caratteri per verso')
plt.ylabel('Occorrenze')

# Calcolo dei valori attesi nel modello Poissoniano e gaussiano. Verificate che la
# definizione di k alla riga qui sotto corrisponde a tutti i valori interi compresi tra
# la minima e la massima lunghezza dei versi. Notate anche la differenza tra le funzioni
# di scipy pmf(), per il calcolo della probabilita` per una distribuzione dicreta, e
# pdf(), per il calcolo della densita` di probabilita` per una continua.
k = np.arange(l.min(), l.max() + 1)
e_poisson = N * poisson.pmf(k, m)
e_gauss = N * norm.pdf(k, m, s)
# Gia` che ci siamo, disegnamo i valori attesi sull'istogramma di partenza.
# Notate che disegnamo la distribuzione di Poisson di best fit come un grafico a barre
# (spostato rigidamente di 0.3 unita` sulla sinistra per far si` che non si sovrapponga
# all'istogramma di partenza) e la distribuzione di Gauss come una linea.
plt.bar(k - 0.3, e_poisson, width=0.25, color='#ff7f0e', label='Poisson')
plt.plot(k, e_gauss, color='#2ca02c', label='Gauss')

# Calcolo del chi quadro nelle due ipotesi. Assicuratevi di capire esattamente perche'
# le due righe seguenti corrispondono all'espressione che abbiamo studiato.
chi2_poisson = ((o - e_poisson)**2. / e_poisson).sum()
chi2_gauss = ((o - e_gauss)**2. / e_gauss).sum()
dof_poisson = len(k) - 1 - 1
dof_gauss = len(k) - 1 - 2
print(f'chi2 per la Poissoniana: {chi2_poisson} / {dof_poisson} dof')
print(f'chi2 per la Gaussiana: {chi2_gauss} / {dof_gauss} dof')

plt.legend()
plt.show()
