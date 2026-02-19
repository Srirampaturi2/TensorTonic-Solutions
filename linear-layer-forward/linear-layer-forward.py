import numpy as np

def linear_layer_forward(X, W, b):
    X = np.array(X)
    W = np.array(W)
    b = np.array(b)
    Y = X @ W + b
    return Y.tolist()