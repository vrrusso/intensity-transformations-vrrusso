#Victor Rodrigues Russo  11218855  SCC025 Image Processing  202001  intensity transformations

import numpy as np
import imageio as im

#transformation no 1 - the inverse of input image
def inversion(input_img):
    return (255-input_img).astype(np.uint8)

#transformation no 2 - tunes out the max and the min of the image
def contrast_modulation(input_img,c,d):
    a = input_img.min()
    b = input_img.max()
    delta = (c-d)/(b-a)
    return (input_img*delta-c).astype(np.uint8)

#this is the main block of code
filename = str(input()).rstrip()
input_img = im.imread(filename)
method = int(input())
transformed_img = np.zeros(input_img.shape).astype(np.uint8)

if method == 1:
    transformed_img = inversion(input_img)
elif method == 2:
    c = int(input())
    d = int(input())
    transformed_img = contrast_modulation(input_img,c,d)
elif method == 3:
    print('logarithm function')
elif methot == 4:
    print('gamma adjustment')
save = int(input())
if save == 1:
    im.imwrite('output_img.png',transformed_img)


