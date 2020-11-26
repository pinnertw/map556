'''
Created on 15 december 2015
MAP556 - Ecole Polytechnique - 3A
@author: emmanuelgobet
'''

import numpy as np
import numpy.random as npr

def inverseFctRepartitionCauchy(x, a):
	return a * np.tan(np.pi * (x-.5))

def MaFonction(C):
#	return np.sin(C) # estimateur antithetique symmetrique est parfait car la fonction est symmetrique
#	return np.cos(C) # estimateur antithetique inverse est bon et pas le symmetrique 
	return (C>0)*np.abs(C)**0.25  # la fonction est croissante mais pas pair (donc pas de gain 2 assure pour l'antithetique inverse)

a = 1
n = 10000

X = npr.rand(n)
C = inverseFctRepartitionCauchy(X, a)

print("Reduction de variance pour variable de Cauchy par technique d'antithetique")
print("Moyenne et ecart-type avec\n")

# echantillon standard
Y=MaFonction(C)
StdY1=np.std(Y)
print(" "*10+"* echantilon standard:")
print(" "*20+"%2.6f, %2.6f"%(np.mean(Y),StdY1))

# echantillon symetrise
Y2=MaFonction(-C)
StdY2=np.std((Y+Y2)*0.5)
print("\n"+" "*10+"* echantilon standard et symmetrise (-C):")
print(" "*20+"%2.6f, %2.6f"%(np.mean((Y+Y2)*0.5),StdY2))

# echantillon inverse
Y3=MaFonction(a**2/C)
StdY3=np.std((Y+Y3)*0.5)
print("\n"+" "*10+"* echantilon standard et inverse (a^2/C):")
print(" "*20+"%2.6f, %2.6f"%(np.mean((Y+Y3)*0.5),StdY3))