# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:49:09 2017
MAP556 - Ecole Polytechnique - 3A
@author: emmanuelgobet
"""

import numpy as np
import matplotlib.pyplot as plt

def ma_fonction_a_integrer(x):
	return np.exp(np.sum(x))

M=100
n=1021 # Korobov rule 4093,2039, 4093
d = 8 # dimension

square_root_prime_numbers=np.sqrt((2,3,5,7,11,13,17,19,23,29,31))

U_QMC=np.zeros((n,d))
for i in np.arange(n):
	for j in np.arange(d):
		U_QMC[i,j]=i*square_root_prime_numbers[j]%1

U_lattice=np.zeros((n, d))
z=np.zeros(d)
a_korobov=14471.0
for i in np.arange(d):
	z[i]=a_korobov**i % n
for m in np.arange(n):
	U_lattice[m,:]=((z*m)/n) %1

plt.close('all')
plt.figure('Scatterplot of lattice points')
for i in np.arange(d):
	for j in np.arange(d):
		plt.subplot(d,d,i*(d)+j+1)
		plt.scatter(U_lattice[:,i],U_lattice[:,j],1)
		plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
plt.tight_layout()

plt.show()

plt.figure('Scatterplot of QMC points')
for i in np.arange(d):
	for j in np.arange(d):
		plt.subplot(d,d,i*(d)+j+1)
		plt.scatter(U_QMC[:,i],U_QMC[:,j],1)
		plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
plt.tight_layout()
plt.show()

output=np.zeros((M,3))
for i in np.arange(M): # MC exterieur
	# calcul interieur: Monte Carlo standard
	U_a_moyenner=np.random.rand(n, d)
	for j in np.arange(n):
		output[i,0]+=ma_fonction_a_integrer(U_a_moyenner[j,:])
	output[i,0]/=n
	# calcul interieur: Quasi Monte Carlo
	U_a_moyenner=(np.random.random()+U_QMC)%1
	for j in np.arange(n):
		output[i,1]+=ma_fonction_a_integrer(U_a_moyenner[j,:])
	output[i,1]/=n
		# calcul interieur: Lattice
	U_a_moyenner=(np.random.random()+U_lattice)%1
	for j in np.arange(n):
		output[i,2]+=ma_fonction_a_integrer(U_a_moyenner[j,:])
	output[i,2]/=n

plt.figure('Comparison of Monte-Carlo estimators')
ecart_type=np.std(output,axis=0) # ecart-type pour les 3 series
for i in np.arange(3):
	moyenne_empirique=np.cumsum(output[:,i])/np.arange(1,M+1)
	ICplus=moyenne_empirique+1.96*ecart_type[i]/np.sqrt(np.arange(1,M+1))
	ICmoins=moyenne_empirique-1.96*ecart_type[i]/np.sqrt(np.arange(1,M+1))
	if i==0:
		mon_label="MC standard"
		ma_couleur="r"
	elif i==1:
		mon_label="QMC"
		ma_couleur="g"
	else:
		
		mon_label="Lattice"
		ma_couleur="b"
#	plt.plot(moyenne_empirique,ma_couleur+"-", lw=2, label=mon_label)
	plt.plot(ICplus,ma_couleur+"-",lw=2,label=mon_label)
	plt.plot(ICmoins,ma_couleur+"-",lw=2)
	
reference_value=(np.exp(1)-1)**d
plt.plot(reference_value*np.ones((M,1)),"k-", lw=2, label= "Reference value d=%1.0f"%d)

plt.ylim((reference_value*0.98,reference_value*1.02))
plt.legend(loc="best")
plt.show()
