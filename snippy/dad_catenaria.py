import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Visualizzazione dell'immagine in matplotlib---va da se': dovete sostituire il
# percorso al file contenente l'immagine con quello appropriato per voi.
# Una volta aperta l'immagine in matplotlib potete andare sopra con il mouse e
# vedrete la posizione (in pixel) visualizzata sulla barra inferiore della finestra.
# Questo vi permette di misurare manualmente la posizione di un numero arbitrario
# di punti nell'immagine stessa.
file_path = '../figures/catenaria.jpg'
plt.figure('Immagine originale')
img = matplotlib.image.imread(file_path)
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.imshow(img)

def catenary(x, a, c, xc):
    """Modello di catenaria.
    """
    return c + a * np.cosh((x - xc) / a)

# Come prima: usate il percorso al vostro file.
file_path = '../macro/data/catenaria.txt'
x, y = np.loadtxt(file_path, unpack=True)
# Ricordate: il riferimento delle immagini, tipicamente, e` in alto a sinistra,
# per cui potreste aver bisogno di cambiare segno alla y.
y = -y
# Fate attenzione alle incertezze: il valore, qui, e` completamente arbitario.
sigma_y = 3.

# Grafico principale.
fig = plt.figure('Fit e residui')
fig.add_axes((0.1, 0.3, 0.8, 0.6))
plt.errorbar(x, y, sigma_y, fmt='o')
# Fit. Notate che, per far convergere il fit, avrete bisogno di fornire una
# stima iniziale ragionevole dei parametri.
popt, pcov = curve_fit(catenary, x, y, p0=(1000., -3000., 2300.))
a0, c0, xc0 = popt
sigma_a, sigma_c, sigma_xc = np.sqrt(pcov.diagonal())
print(a0, sigma_a, c0, sigma_c, xc0, sigma_xc)
plt.plot(x, catenary(x, a0, c0, xc0))
plt.grid(which='both', ls='dashed', color='gray')
plt.ylabel('y [u. a.]')

# Grafico dei residui.
fig.add_axes((0.1, 0.1, 0.8, 0.2))
res = y - catenary(x, a0, c0, xc0)
plt.errorbar(x, res, sigma_y, fmt='o')
plt.grid(which='both', ls='dashed', color='gray')
plt.xlabel('x [u. a.]')
plt.ylabel('Residuals')
plt.ylim(-20.0, 20.0)
plt.savefig('catenaria.pdf')

plt.show()
