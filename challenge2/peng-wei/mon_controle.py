import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np

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
a.load_weights("td3_actor_60")
a(tf.convert_to_tensor([[0., 0., 0.]]))
def main(seconde, position):
    force=np.array([-(position[0]-10.*seconde),-(position[1]-(20.*seconde-2*seconde** 2))]) 
    force+=a(tf.convert_to_tensor([[seconde/10, position[0]/100, position[1]/50]], dtype=tf.float32)).numpy()[0]
    #print(force)
    return force
'''
def main(seconde, position):
        return np.array([-(position[0]-10.*seconde),-(position[1]-(20.*seconde-2*seconde** 2))])
'''
