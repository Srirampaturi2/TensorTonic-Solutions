import numpy as np 
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    #image= [[[255,0,0]]]
    image= np.array(image)
    R= image[:,:,0]
    G= image[:,:,1]
    B=  image[:,:,2]
    gray_img = 0.299* R + 0.587 * G +0.114 * B 
    return gray_img.tolist()
    
    
    