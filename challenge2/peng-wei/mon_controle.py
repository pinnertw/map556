import numpy as np
coeffs = np.load("cc.npy")
coeffs2 = np.load("cc2.npy")
mean_states = np.load("mean_states.npy")
cor = np.array([[0, 0, 0],
               [0, 3, 2],
               [0, 1, 0]])
seconds = np.arange(11)
pos = np.zeros((11, 2))
pos[:, 0] = seconds * 10
pos[:, 1] = seconds * 20 - 2 * seconds**2
def main(seconde, position):
    t = int(seconde)
    a, b =np.sign(position - mean_states[t]).astype(int)
    i = cor[a][b]
    if t < 9:
        return coeffs[t, i, :2]*pos[t]-coeffs[t, i, 2:4]*position + coeffs[t, i, 4:]
    else:
        return coeffs[t, i, :2]*pos[t]-coeffs[t, i, 2:4]*position + coeffs[t, i, 4:] + coeffs2*position**2*(i < 0.5)
