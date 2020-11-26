import numpy as np
import tensorflow as tf

class Actor(tf.keras.Model):
    def __init__(self, no_action):
        super(Actor, self).__init__()
        self.f1 = tf.keras.layers.Dense(64, bias_initializer='zeros', kernel_initializer='zeros', activation='relu')
        self.f2 = tf.keras.layers.Dense(64, bias_initializer='zeros', kernel_initializer='zeros', activation='relu')
        self.mu =  tf.keras.layers.Dense(no_action, activation=None)

    def call(self, state):
        x = self.f1(state)
        x = self.f2(x)
        x = self.mu(x)
        return x

a = Actor(2)
a.load_weights("td3_actor")

def exemple_model(seconde, position):
#    return np.array([np.sin(seconde), np.cos(position[0] + position[1])])
    return a.call(tf.convert_to_tensor([[seconde, position[0], position[1]]], dtype=tf.float32)).numpy()[0]


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
