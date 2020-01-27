import cv2
import numpy as np
import core.image as im
import matplotlib.pyplot as plt

pi = np.pi
theta_set = [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4]

# Fixed variable
fx_scale = 31
fx_sigma = 5
fx_lambda = 9
fx_gamma = 1


def genKernel(theta):

    # Dynamic variable
    d_theta = theta

    # Get Kernale
    gabor_k = cv2.getGaborKernel((fx_scale, fx_scale), fx_sigma, d_theta, fx_lambda, fx_gamma, 0, ktype=cv2.CV_32F)

    # Size incresing for displaying
    scale = 9
    (h, w) = gabor_k.shape
    re_gabor_k = cv2.resize(gabor_k, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

    # Displaying
    # cv2.imshow('Kernal with Resizing, theta={}'.format(d_theta), re_gabor_k)

    print('Theta:', d_theta)
    print('gabor_k:', gabor_k.shape)
    print('re_gabor_k:', re_gabor_k.shape)

    return gabor_k

if __name__ == '__main__':
    img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_12.tif'
    imgs = im.getImage(img_path, display=False)

    # Pyramids Image
    pyr_imgs = im.multiPyrDown(imgs[1], debug=True)

    invar_k = np.ndarray(shape=(fx_scale, fx_scale))

    for theta in theta_set:
        temp_k = np.asarray(genKernel(theta))
        invar_k = np.add(invar_k, temp_k)

    (h, w) = invar_k.shape
    scale = 10
    re_invar_k = cv2.resize(invar_k, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

    # Filtering
    # filtered_img = cv2.filter2D(pyr_imgs[1], -1, invar_k)

    cv2.imshow('OIKernel', re_invar_k)
    # cv2.imshow('Fitered', filtered_img)
    cv2.waitKey()
