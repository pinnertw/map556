import numpy as np
coeffs = np.load("c_60.npy")                    #coeffs : the coefficients for all the members in the equation
pos = np.load("mean_states_1440.npy")     #pos : the average position at t=0 to t=9
sqr2 = 1/np.sqrt(2)
rot = np.array([[sqr2, -sqr2],
               [sqr2, sqr2]])                #rot : the rotation matrix to rotate 45 degrees counter-clockwise
rot2 = np.array([[sqr2, sqr2], [-sqr2, sqr2]]) #rot2 : rotation 45 degrees clockwise
def main(seconde, position):
    t = int(seconde)
    x1, x2 = np.matmul(rot, position - pos[t])
    u1 = np.array([x1*(x1>0), x2*(x2>0)])
    u2 = np.array([x1*(x1<0), x2*(x2<0)])
    return np.matmul(rot2, coeffs[t,:2]*u1 + coeffs[t,2:4]*u2 + coeffs[t,4:6])