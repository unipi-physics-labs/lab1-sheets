# Programma di esempio per l'analisi del file prodotto dal simulatore
# del lancio di dadi.
#
# (Le linee precedute da un cancelletto sono commenti per illustrare il codice,
# non e` necessario che le copiate nei vostri programmi.)


import pylab

# Definizione di alcune variabili (da cambiare a piacimento).
n_dadi  = 2
n_lanci = 1000

# Lettura del file di dati in ingresso (da modificare con il percorso al
# vostro file in ingresso).
valori, occorrenze = pylab.loadtxt( 'data/plasduino_dice.txt', unpack = True)

# Calcolo della media e varianza campione.
media_campione = sum(occorrenze*valori)/n_lanci
varianza_campione = sum(occorrenze*((valori - media_campione)**2))/(n_lanci - 1)
dev_standard_campione = pylab.sqrt(varianza_campione)
print('m = %f, s = %f' % (media_campione, dev_standard_campione))

# Realizzazione e salvataggio del grafico.
pylab.title('%d lanci di %d dado/i' % (n_lanci, n_dadi))
pylab.xlabel('Somma delle uscite') 
pylab.ylabel('Occorrenze')
pylab.grid()
pylab.bar(valori, occorrenze, 1)
pylab.savefig('dice_%d_%d.pdf' % (n_dadi, n_lanci))

pylab.show()
