import cv2
import numpy as np
import matplotlib.pyplot as plt


def grid_plot(data, size, title='Untitle', is_img=False):
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    length = size**2
    graphs = []

    for i in range(1, length+1):
        temp_plt = fig.add_subplot(size, size, i)
        graphs.append(temp_plt)

    for i, d in enumerate(data):
        try:
            graphs[i].imshow(d, cmap=plt.cm.gray)
        except IndexError:
            break


# sigma = the standard deviation of the Gaussian function used in the Gabor filter.
# theta = the orientation of the normal to the parallel stripes of the Gabor function.
# lambda = the wavelength of the sinusoidal factor in the above equation.
# gamma = the spatial aspect ratio.
# psi = the phase offset.
# ktype = indicates the type and range of values that each pixel in the Gabor kernel can hold.

grid = []

for dx in np.arange(0.5, 5, 0.5):
    _usize = 9
    _ksize = (_usize, _usize)
    _sigma = 0 + dx
    _theta = 0
    _lambda = 4
    _gamma = 1.0
    _psi = 0
    _ktype = cv2.CV_32F

    gabor_k = cv2.getGaborKernel(
        _ksize, _sigma, _theta,
        _lambda, _gamma, _psi,
        _ktype
    )

    h, w = gabor_k.shape[:2]
    gabor_k_show = cv2.resize(gabor_k, (100*w, 100*h), interpolation=cv2.INTER_CUBIC)
    grid.append(gabor_k_show)


size = np.int(np.round(np.sqrt(len(grid))))
grid_plot(grid, size, title='Gabor Kernel', is_img=True)
plt.show()
