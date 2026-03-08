def histogram_equalize(image):
    H = len(image)
    W = len(image[0])
    total_pixels = H * W

    # Step 1: Histogram
    histogram = [0] * 256
    for row in image:
        for pixel in row:
            histogram[pixel] += 1

    # Step 2: CDF
    cdf = [0] * 256   # [0,0,0,0.............256]
    cdf[0] = histogram[0]  # intensity = 10
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + histogram[i]  # calc no of non-zero pixels so far

    # Step 3: cdf_min (first non-zero)
    cdf_min = next(c for c in cdf if c > 0)   # gets the first min non-zero darkest pixel 
    if total_pixels == cdf_min:
         return [[0]*W for _ in range(H)]
    # Step 4: Map each pixel
    result = [[0]*W for _ in range(H)]   #[0,0,0,0,0,0] 
    for i in range(H):
        for j in range(W):
            v = image[i][j]
            result[i][j] = round((cdf[v] - cdf_min) / (total_pixels - cdf_min) *255)
    return result