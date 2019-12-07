import cv2
import numpy as np

# sigma = the standard deviation of the Gaussian function used in the Gabor filter.
# theta = the orientation of the normal to the parallel stripes of the Gabor function.
# lambda = the wavelength of the sinusoidal factor in the above equation.
# gamma = the spatial aspect ratio.
# psi = the phase offset.
# ktype = indicates the type and range of values that each pixel in the Gabor kernel can hold.

pi = np.pi
gaborParams = {
    'scale': [61, 33, 13, 9],
    'theta': [0, pi/8, 2*pi/8, 3*pi/8, 4*pi/8, 5*pi/8, 6*pi/8, 7*pi/8, 8*pi/8], #8
    # 'lambda': [4, 4*np.sqrt(2), 8, 8*np.sqrt(2), 16]
    'lambda': [1, 2, 4, 8, 16, 32 ,64] # 7
}

def getKernel(_scale):
    _gamma = 1
    _psi = 0
    _ktype = cv2.CV_32F
    _kernels = []

    for _theta in gaborParams['theta']:
        for _lambda in gaborParams['lambda']:
            _ksize = (_scale, _scale)
            _sigma = _theta
            gabor_k = cv2.getGaborKernel(
                _ksize, _sigma, _theta,
                _lambda, _gamma, _psi,
                _ktype
            )
            _kernels.append(gabor_k)

    return _kernels 


if __name__ == '__main__':
    filters = getKernel(61)
    print(filters)
