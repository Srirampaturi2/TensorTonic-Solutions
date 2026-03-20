import numpy as np
def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
      
    H = len(image)
    W = len(image[0])
    
    pad_h = len(kernel) // 2
    pad_w = len(kernel[0]) // 2
    kh   = len(kernel)
    kw= len(kernel[0])
    
    img = np.array(image)
    padded = np.zeros((H + 2*pad_h, W + 2*pad_w), dtype=img.dtype)
    padded[pad_h:pad_h+H, pad_w:pad_w+W] = img  #  starting after the zero border, paste the original image into the center! 
    result= []
    for i in range(H):
        row = []
        for j in range(W):
            patch = padded[i:i+kh, j:j+kw]
            if operation == "erode":
                val = 1
                for ki in range(kh):
                    for kj in range(kw):
                        if kernel[ki][kj] == 1 and patch[ki][kj] == 0:
                            val = 0
                            break
                    if val == 0:
                        break
            else:  # dilate
                val = 0
                for ki in range(kh):
                    for kj in range(kw):
                        if kernel[ki][kj] == 1 and patch[ki][kj] == 1:
                            val = 1
                            break
                    if val == 1:
                        break
            row.append(val)
        result.append(row)
    return result
'''
   My initial design: patch = padded[1:1+3, 1:1+3]  # Building patch to compare with the kernel
    for i,j in range(patch.shape()):
        if ( kernel[i][j] == patch[i][j])
           ouput = 0
'''