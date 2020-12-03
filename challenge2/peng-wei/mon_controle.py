import numpy as np
coeffs = np.load("css.npy")
seconds = np.arange(11)
pos = np.zeros((11, 2))
pos[:, 0] = seconds * 10
pos[:, 1] = seconds * 20 - 2 * seconds**2
def main(seconde, position):
    t = int(seconde)
    s = t
    #print(seconde, position, pos[t])
    return coeffs[s, :2]*pos[t]-coeffs[s, 2:4]*position + coeffs[s, 4:]
