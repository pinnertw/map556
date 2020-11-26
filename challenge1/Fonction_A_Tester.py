#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 2020
Code Etudiant
@author: Michael Allouche, Emmanuel Gobet
MAP556, Methodes de Monte Carlo: du lineaire au non-linéiare
"""


import numpy as np
import sys

def fonction_test(x, label="fake"):
    """
    input: current point x as np.array
           label describing the test function (not used by studends only by teachers)
    output: numerical value of the function "label" at point "x"
    """
    try:
        assert x.shape[0] == 4  # les gaussiennes doivent etre de dimension 4
    except AssertionError:
        print("Attention, la dimension des donnees est trop grande. Veuillez respecter la consigne.")
        sys.exit(1)

    # exemple fictif de fonction test: sin(x0 + x1**2 + x2**3 + x3**4)
    if label == "fake":
        s=0
        for i in range(4):
            s += x[i]**(i+1)
        s = np.sin(s)
    elif label == "1":
        s = 0
        for i in range(4):
            s += x[i]
    elif label == "2":
        s = 0
        for i in range(4):
            s += np.maximum(np.abs(x[i]) - 1.5, 0)
    elif label == "3":
        s=0
        for i in range(4):
            s += x[i]**(i+1)
        s = np.sin(s)
    elif label == "4":
        s = np.linalg.norm([x[0], x[1]/100, x[2], x[3]/10])
        s = np.sin(s) / (s + 10**-6) + 4
    elif label == "5":
        s = (x[0] + x[1] + x[2] + x[3] > 0.5)
    elif label == "6":
        s = (x[0] + x[1] + x[2] + x[3] > 0.0)
    elif label == "7":
        s = np.sum(x)
        if s<=0:
            s = 0
        else:
            s += 1
    elif label == "8":
        s = np.sin(np.sqrt(x.dot(x))) / (np.sqrt(x.dot(x))+1)
    elif label == "9":
        s = 100 * np.exp(-(x-3).dot(x-3))
    elif label == "10":
        s = np.exp(-x.dot(x)/10)
    elif label == "11":
        s = x.dot(x)
    elif label == "12":
        s = np.abs(x[0]) + x[1]
    elif label == "13":
        s = x[1] + 2 * x[1] ** 2 + 4 * x[1] ** 6
    elif label == "14":
        s = np.cos(np.sum(x))
    elif label == "15":
        s = 0
        for i in range(4):
            s += x[i] ** (i+1)
    elif label == "16":
        s = 0
        for i in range(4):
            s += x[i] ** (2 * i + 2)
        s = np.sqrt(s)
    elif label == "17":
        s = 0
        for i in range(4):
            s += x[i]**(2 * i + 2)
        s = 1 / (1 + s)
    elif label == "18":
        s = np.linalg.norm(x)
    elif label == "19":
        s = np.linalg.norm(x) ** 2
    elif label == "20":
        s = 0
        for i in range(4):
            s += int(x[i] < 0)
    elif label == "21":
        s = 1
        for i in range(4):
            s *= x[i]
    elif label == "22":
        s = 1
        for i in range(4):
            s *= x[i] ** 2
    elif label == "23":
        s = 0
        for i in range(4):
            s += np.abs(x[i])
        s = np.log(s)
    elif label == "24":
        s = 0
        for i in range(4):
            s += np.log(1 + np.abs(x[i]))
    return s
