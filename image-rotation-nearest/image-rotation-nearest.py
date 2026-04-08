import math 
def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here  1. 
    H = len(image)
    W= len(image[0])
    rad_val=  math.radians(angle_degrees)
    cx = (W-1)/2
    cy = (H-1)/2
    out = []
     # Offets from center 
    for i in range(H):
        row=[]
        for j in range(W):
             dy = i -cy  # Rotation distance from center 
             dx = j-cx
             src_y = round(cy+ dy*(math.cos(rad_val))  + dx*(math.sin(rad_val)) ) # New co-ordinate index change 
             src_x = round(cx- dy*(math.sin(rad_val)) + dx*(math.cos(rad_val)))
             if 0 <= src_y < H and 0 <= src_x < W:
               row.append(image[src_y][src_x])
             else:
               row.append(0)
        out.append(row)
    return out
    