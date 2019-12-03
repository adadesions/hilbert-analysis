from . import gaborParams
import cv2
import numpy as np

# sigma = the standard deviation of the Gaussian function used in the Gabor filter.
# theta = the orientation of the normal to the parallel stripes of the Gabor function.
# lambda = the wavelength of the sinusoidal factor in the above equation.
# gamma = the spatial aspect ratio.
# psi = the phase offset.
# ktype = indicates the type and range of values that each pixel in the Gabor kernel can hold.

# lambdaParams = [1, 1.5, 2.0, 2.5, 3.0, 3.5]
# thetaParams = [0, pi/6, pi/4, pi/3, pi/2, pi, 2*pi/3, 3*pi/4, 5*pi/6, pi]


def getKernel(_sigma, _lambda):
    _gamma = 1
    _psi = 0
    _ktype = cv2.CV_32F
    kernels = []

    for idx, params in enumerate(gaborParams):
        _ksize = (params['scale'], params['scale'])
        _theta = params['theta']
        gabor_k = cv2.getGaborKernel(
            _ksize, _sigma, _theta,
            _lambda, _gamma, _psi,
            _ktype
        )
        kernels.append(gabor_k)

    return kernels 
