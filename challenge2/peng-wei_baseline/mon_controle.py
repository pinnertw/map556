import numpy as np
import tensorflow as tf

meanx = np.load("meanx.npy")
meany = np.load("meany.npy")
stdx = np.load("stdx.npy")
stdy = np.load("stdy.npy")
coeff = 0.0249

def exemple_model(seconde, position):
    i = seconde
    if i == 0:
        return np.array([0., 0.])
    else:
        force = np.array([-(position[0] - meanx[i-1]) * coeff * stdx[i-1], 
                          -(position[1] - meany[i-1]) * coeff * stdy[i-1]])
        return force


def main(seconde, position):
    """
    Votre controle du AG 2.0 au temps t seconde(s) et à la position X_t

    Parameters
    ----------
    seconde: float
        s = 0., 1., .., 9.
    position: arr (2,)
        Position du AG de format (2,) avec coordonnée x = position [0] et coordonnée y = position [1]

    Returns
    -------
    arr (2,)
        Contrôle du AG durant la prochaine seconde.

    Notes
    ----
    La sortie de cette fontion doit être la valeur de votre contrôle :
        un array (de float32 ou float64) et de dimension (2,)

    """
    return exemple_model(seconde, position)
