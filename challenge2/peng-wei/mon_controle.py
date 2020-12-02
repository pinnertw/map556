import numpy as np
m=np.load("umat.npy")
db1=np.load("db1.npy")
db2=np.load("db2.npy")
ub1=np.load("ub1.npy")
ub2=np.load("ub2.npy")
def main(seconde, position):
    s=int(seconde)
    x,y=position
    force=1.59*(np.array([10*s,20*s-2*s**2])-1.0125*position)
    if t==0:
        return m[0][0][0]+force
    else:
        i1=min(max(int((x1-db1[t-1])/(ub1[t-1]-db1[t-1])*2*t),0),2*t-1)
        i2=min(max(int((x2-db2[t-1])/(ub2[t-1]-db2[t-1])*2*t),0),2*t-1)
        return mat[t][i1][i2]+force