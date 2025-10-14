import wave

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

file_path = 'macro/data/bouncing_ball3.wav'
# Apertura del file audio, vedi https://docs.python.org/3/library/wave.html
stream = wave.open(file_path)
signal = np.frombuffer(stream.readframes(stream.getnframes()), dtype=np.int16)
# Importante: se il file originale e` stereo dobbiamo prendere solo uno dei canali.
if stream.getnchannels() == 2:
    signal = signal[::2]
# L'unica cosa che ci manca e` l'array dei tempi corrispondenti ai singoli campioni.
t = np.arange(len(signal)) / stream.getframerate()

# A questo punto siamo pronti per analizzare il tracciato audio. Una volta
# messi i dati in un grafico di matplotlib possiamo utilizzare lo strumento
# zoom ed il mouse per misurare i tempi di rimbalzo della pallina.
plt.figure('Rimbalzi pallina')
plt.plot(t, signal)
plt.xlabel('Tempo [s]')
plt.savefig('audio_rimbalzi.pdf')

# Supponiamo di aver preso a mano questa serie di tempi di rimbalzo.
t = [0.01961451, 0.69562358, 1.23981859, 1.679161, 2.04113379, 2.33979592]
# Cercate di stimare ragionevolmente gli errori...
sigma_t = 0.005
# Calcolo delle differenze di tempo.
dt = np.diff(t)
# Creazione dell'array con gli indici dei rimbalzi.
n = np.arange(len(dt)) + 1.
# Calcolo dell'altezza massima e propagazione degli errori.
h = 9.81 * (dt**2.) / 8.0
dh = 2.0 * np.sqrt(2.0) * h * sigma_t / dt

def expo(n, h0, gamma):
    """Modello di fit.
    """
    return h0 * gamma**n

plt.figure('Altezza dei rimbalzi')
plt.errorbar(n, h, dh, fmt='o')
popt, pcov = curve_fit(expo, n, h, sigma=dh)
h0_hat, gamma_hat = popt
sigma_h0, sigma_gamma = np.sqrt(pcov.diagonal())
print(h0_hat, sigma_h0, gamma_hat, sigma_gamma)
x = np.linspace(0.0, 6.0, 100)
plt.plot(x, expo(x, h0_hat, gamma_hat))
plt.yscale('log')
plt.grid(which='both', ls='dashed', color='gray')
plt.xlabel('Rimbalzo')
plt.ylabel('Altezza massima [m]')
plt.savefig('altezza_rimbalzi.pdf')

plt.show()
