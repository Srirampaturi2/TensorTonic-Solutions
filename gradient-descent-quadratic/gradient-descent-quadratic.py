def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here f'(x)= 0 
    x=x0
    for i in  range(steps):
       x= x - lr*(2*a*x + b)
    
    return x
    