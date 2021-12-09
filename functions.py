import numpy as np

def sigmoid (x):
    return 1 / (1 + np.exp(-x))

def seuil (x):
    x[x <= 0.4] = 0.  # low
    x[x <= 0.7] = 0.5 # medium
    x[x > 0.7]  = 1.  # high
    return x
