import math
import numpy as np 

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    l=math.sqrt(6/fan_in)
    W= np.array(W)
    W_new = (W * (2*l))-l # Maps back b/w -1 to 1 
    return W_new
