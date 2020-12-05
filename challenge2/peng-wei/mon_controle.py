import numpy as np
coeffs = np.load("c_720.npy")                    #coeffs : the coefficients for all the members in the equation
mean_states = np.load("mean_states_720.npy")     #mean_states : the average position at t=0 to t=9
quantiles = np.load("quantiles_720.npy")         #the quantiles for the axes after being rotated from y=-x+h(t) to axe x
seconds = np.arange(11)
pos = np.zeros((11, 2))                      #pos : the position where the birds should be at different t.
pos[:, 0] = seconds * 10
pos[:, 1] = seconds * 20 - 2 * seconds**2
sqr2 = 1/np.sqrt(2)
rot = np.array([[sqr2, -sqr2],
               [sqr2, sqr2]])                #rot : the rotation matrix to rotate 45 degrees counter-clockwise
def main(seconde, position):
    t = int(seconde)
    a, _ = rot.dot(position - mean_states[t])
    i = np.searchsorted(quantiles[:, t],a, side="left")
    return coeffs[t, i, :2]*pos[t]-coeffs[t, i, 2:4]*position + coeffs[t, i, 4:]
