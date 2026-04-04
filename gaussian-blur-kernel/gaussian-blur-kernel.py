import math

def gaussian_kernel(size, sigma):
    center = size // 2
    kernel = []
    
    for i in range(size):
        row = []
        for j in range(size):
            x = j - center
            y = i - center
            G = pow(math.e, -(x*x + y*y) / (2 * sigma*sigma))
            row.append(G)
        kernel.append(row)  # Appends All rows into a kernel list 
    
    # Normalize
    total = sum(sum(row) for row in kernel)
    kernel = [[val/total for val in row] for row in kernel]
    
    return kernel