import cv2
import numpy as np
import core.image as im
import core.hc_extender as hc_ext


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


# Initialization
img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_12.tif'
imgs = im.getImage(img_path, display=False)
d_scale = 60
d_sigma = 3
d_lambda = 2
d_gamma = 1
d_theta = 180
global_img = imgs[1]


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

    # Get Hilbert Curve Coordinate with Order k
    k = int(np.log2(imgs[0].shape[0]))
    print('Hilbert Curve Order', k)
    hcc = hc_ext.get_hc_index(order=k)

    # VHC <-- Vector of Hilbert Curve
    vhc = trans(imgs[1], hcc)


    while True:
        # Get Kernal
        gabor_k = cv2.getGaborKernel((d_scale, d_scale), d_sigma, d_theta, d_lambda, d_gamma, 0, ktype=cv2.CV_32F)

        # Filtering
        global_img = cv2.filter2D(imgs[1], -1, gabor_k)

        cv2.imshow('A', global_img)
        cv2.waitKey(1)
