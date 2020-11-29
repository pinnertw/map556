import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
'''
import tensorflow as tf
class Actor(tf.keras.Model):
    def __init__(self, no_action):
        super(Actor, self).__init__()
        self.f1 = tf.keras.layers.Dense(40, activation='relu')
        self.f2 = tf.keras.layers.Dense(40, activation='relu')
        self.mu =  tf.keras.layers.Dense(no_action, activation=None)
    def call(self, state):
        x = self.f1(state)
        x = self.f2(x)
        x = self.mu(x)
        return x
a = Actor(2)
a.load_weights("td3_actor_55000")
def main(seconde, position):
    seconde/=10
    position/=np.array([100., 50.])
    force = a(tf.convert_to_tensor([[seconde, position[0], position[1]]], dtype=tf.float32)).numpy()[0]
    print(seconde, position, force)
    return force
'''
def main(seconde, position):
        return np.array([-(position[0]-10.*seconde),-(position[1]-(20.*seconde-2*seconde** 2))])
