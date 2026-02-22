import numpy as np
def dot_product(x, y):
    x = np.array(x)
    y = np.array(y)
    if len(x) != len(y):
        raise ValueError(f"Against Maths Universe Laws check dims :{len(x)},{len(y)}")
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return float(sum)