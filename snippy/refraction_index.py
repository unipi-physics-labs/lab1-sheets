# Programma di esempio per l'analisi delle misure sull'indice di rifrazione di acqua e plexiglass
import pylab
from scipy.optimize import curve_fit

# Dati in ingresso per il diottro (da modificare con le vostre misure).
p = pylab.array([45.6, 42.9, 41.0, 38.7, 35.8, 34.1], 'd')
q = pylab.array([43.5, 47.6, 51.2, 56.4, 68.1, 75.4], 'd')
Dp = pylab.array(len(p)*[0.5],'d')
Dq = pylab.array(len(q)*[1],'d')

# Plot di 1/q vs 1/p
pylab.figure(1)
pylab.title('Indice di rifrazione dell\'acqua')
pylab.xlabel('1/p [1/cm]') 
pylab.ylabel('1/q [1/cm]') 
pylab.grid(color = 'gray')
pylab.errorbar(1./p, 1/q, Dp/(p*p), Dq/(q*q), 'o', color='black' )

# Fit con una retta - nota che le incertezze sono ignorate!
def f(x, a, b):
    return a*x + b

popt, pcov = curve_fit(f, 1./p, 1/q, pylab.array([-1.,1.]))
a, b       = popt
da, db     = pylab.sqrt(pcov.diagonal())
print('Acqua: n = %f +- %f' % (a, da))
pylab.plot(1./p, f(1./p, a, b), color='black' )
pylab.savefig('rifrazione_acqua.png')

# Dati in ingresso per il plexiglass (da modificare con le vostre misure).
# In questo esempio x = R*sin(theta_r), y = R*sin(theta_i) [cm]
x = pylab.array([1.25, 1.85, 2.9, 4.35, 0.5,  0.25, 0.8, 1.5, 4.8], 'd')
y = pylab.array([1.9,  2.5,  4.2, 6.65, 0.75, 0.45, 1.1, 2.4, 7. ], 'd')
Dx = pylab.array(len(x)*[0.1],'d')
Dy = pylab.array(len(y)*[0.1],'d')

# Plot di x vs y
pylab.figure(2)
pylab.title('Indice di rifrazione del plexiglass')
pylab.xlabel('R sin(theta_r) [cm]') 
pylab.ylabel('R sin(theta_i) [cm]') 
pylab.grid(color = 'gray')
pylab.errorbar(x, y, Dx, Dy, 'o', color='black' )

# Fit con una retta per essere sicuri che il termine noto sia compatibile con zero
popt, pcov = curve_fit(f, x, y, pylab.array([1.,0.]))
a, b       = popt
da, db     = pylab.sqrt(pcov.diagonal())
print('Plexiglass: b = %f +- %f compatibile con 0?' % (b, db))

# Fit con la legge di Snell
def f1(x, a):
    return a*x

popt, pcov = curve_fit(f1, x, y, pylab.array([1.]))
print('Plexiglass: n = %f +- %f' % (popt, pylab.sqrt(pcov.diagonal())))
pylab.plot(x, f1(x, a), color='black' )
pylab.savefig('rifrazione_plexiglass.png')

pylab.show()

