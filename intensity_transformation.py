#Victor Rodrigues Russo  11218855  SCC025 Image Processing  202001  intensity transformations

import numpy as np
import imageio as im

#transformation no 1 - the inverse of input image - returns the trasnformed image matrix ready to write
def inversion(input_img):
    return (255-input_img)

#transformation no 2 - tunes out the max and the min of the image - returns the transformed image matrix ready to write
def contrast_modulation(input_img,c,d):
    a = input_img.min()
    b = input_img.max()
    delta = float(d-c)/float(b-a)
    return ((input_img-a)*delta + c).astype(np.uint8)

#transformation no 4 - applies a gamma adjustment to the image - returns the transformed image ready to write
def gamma_adjustment(input_img,w,gamma):
    R = 255.0 #the max gray level
    return (np.power(w*(input_img.astype(np.float))/R,gamma)*R).astype(np.uint8)

#evaluates the squared root error off the transformation - returns the error as a numpy float64
def rse_evaluate(input_img,transformed_img):
    size = input_img.shape
    sum=0.0
    for i in range(size[0]):
        for j in range(size[1]):
            sum += np.power((float(transformed_img[i][j])-float(input_img[i][j])),2)
    return np.sqrt(sum)


#this is the main block of code
filename = str(input()).rstrip()
input_img = im.imread(filename)
method = int(input())
save = int(input())
transformed_img = np.zeros(input_img.shape).astype(np.uint8)

if method == 1:
    transformed_img = inversion(input_img)
elif method == 2:
    c = int(input())
    d = int(input())
    transformed_img = contrast_modulation(input_img,c,d)
elif method == 3:
    print('logarithm function')
elif method == 4:
    w = int(input())
    gamma = float(input())
    transformed_img = gamma_adjustment(input_img,w,gamma)

print('{0:.4f}'.format(float(rse_evaluate(input_img,transformed_img))))


if save == 1:
    im.imwrite('output_img.png',transformed_img)