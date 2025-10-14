import random
import numpy as np

# Potete generare un singolo numero pseudo-casuale distributo uniformemente tra 0
# e 2 pi con il modulo random, parte della libreria standard di Python.
# Questo non è molto efficiente, ma va bene per rappresentare graficamente un
# random walk.

phi = random.uniform(0., 2. * np.pi)

# Se siete interessati a generare un random walk e l'unica cosa che vi interessa
# è tenere traccia della posizione finale della particella dopo n passi, è molto
# più efficiente vettorizzare l'operazione utilizzando il modulo random di numpy,
# che permette di generare array di numeri casuali

def random_walk(num_steps):
    """Vectorized 2-dimensional random walk.

    This generates num_steps random angles in the plane, and returns the final
    position of the particle, assuming a unitary step length.
    """
    # Extract an array with num_steps angles equidistributed between 0 and 2 pi.
    phi = np.random.uniform(0., 2. * np.pi, num_steps)
    # Calculate the displacemente along the two orthogonal axes at each step.
    dx = np.cos(phi)
    dy = np.sin(phi)
    # Sum all the displacements to get the final position.
    x = dx.sum()
    y = dy.sum()
    # Return the final position.
    return (x, y)
