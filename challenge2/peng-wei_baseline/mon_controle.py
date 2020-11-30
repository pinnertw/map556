import os
import numpy as np
def main(seconde, position):
    force=np.array([-(position[0]-10.*seconde),-(position[1]-(20.*seconde-2*seconde** 2))]) 
    return force
