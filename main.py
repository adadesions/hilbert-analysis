import cv2
import numpy as np
import core.image as im
import core.hc_extender as hc_ext
import matplotlib.pyplot as plt
from drawnow import drawnow


def trans(img, hcc):
    '''
        trans(img, hcc):
            2D to 1D Transformed by Hilbert Curve

        img <-- nxn matrix
        hcc <-- Hibert curve coordinate with order k
        k <-- 4^log2(n) or nxn, length of hcc
    '''

    result = []
    k = len(hcc)

    for i in np.arange(k):
        (x, y) = hcc[i]
        try:
            val_img = img[x][y]
            result.append(val_img)
        except IndexError:
            continue

    return result


def _change_scale(value):
    global d_scale
    d_scale = value


def _change_sigma(value):
    global d_sigma
    d_sigma = value


def _change_lambda(value):
    global d_lambda
    d_lambda = value


def _change_theta(value):
    global d_theta
    d_theta = value

def _change_gamma(value):
    global d_gamma
    d_gamma = value

def plot_feature():
    plt.plot(vhc)


# Initialization
img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_12.tif'
imgs = im.getImage(img_path, display=False)
d_scale = 9
d_sigma = 3
d_lambda = 8
d_gamma = 1
d_theta = 180
vhc = []
global_img = imgs[1]
(w, h) = imgs[1].shape



if __name__ == "__main__":
    # Setting GUI
    cv2.namedWindow('Original Image')
    cv2.imshow('Original Image', imgs[1])

    # Window A
    cv2.namedWindow('A')
    cv2.createTrackbar('Scale', 'A', d_scale, 128, _change_scale)
    cv2.createTrackbar('Sigma', 'A', d_sigma, 20, _change_sigma)
    cv2.createTrackbar('Lambda', 'A', d_lambda, 100, _change_lambda)
    cv2.createTrackbar('Theta', 'A', d_theta, 360, _change_theta)
    cv2.createTrackbar('Gamma', 'A', d_gamma, 100, _change_gamma)

    # Pyramids Image
    pyr_imgs = im.multiPyrDown(global_img, debug=True)

    # Get Hilbert Curve Coordinate with Order k
    k = int(np.log2(global_img.shape[0]))
    hcc = hc_ext.get_hc_index(order=k)
    print('Hilbert Curve Order', k)
    print('Current Mod Img shape:', global_img.shape)

    while True:
        # Get Kernal
        gabor_k = cv2.getGaborKernel((d_scale, d_scale), d_sigma, d_theta, d_lambda, d_gamma, 0, ktype=cv2.CV_32F)

        # Filtering
        global_img = cv2.filter2D(pyr_imgs[3], -1, gabor_k)

        # VHC <-- Vector of Hilbert Curve
        vhc = trans(global_img, hcc)

        # Display an image and Plotting graph
        cv2.imshow('A', global_img)
        drawnow(plot_feature)

        # Key controller
        key = cv2.waitKey(1) & 0xff
        if key == 27:
            print("End Application")
            break
