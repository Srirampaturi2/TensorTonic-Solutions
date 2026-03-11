def bilinear_resize(image, new_h, new_w):
    H = len(image)
    W = len(image[0])
    result = []
    for i in range(new_h):
        row = [] 
        for j in range(new_w):
            src_y = 0 if new_h == 1 else i * (H - 1) / (new_h - 1)   # Constraints 
            src_x = 0 if new_w == 1 else j * (W - 1) / (new_w - 1)
            y0 = int(src_y)
            x0 = int(src_x)
            dy = src_y - y0
            dx = src_x - x0
            y1 = min(y0 + 1, H - 1)    # Edges 
            x1 = min(x0 + 1, W - 1)
            val = (image[y0][x0] * (1 - dy) * (1 - dx) +
                   image[y1][x0] * dy * (1 - dx) +
                   image[y0][x1] * (1 - dy) * dx +
                   image[y1][x1] * dy * dx)
            row.append(float(val))   # Firslty for appends only each  rows -- 1 Dim 
        result.append(row)    # Appends all rows - 2 Dim 
    return result
