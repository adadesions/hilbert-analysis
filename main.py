import cv2
import numpy as np
import matplotlib.pyplot as plt
import core.image as im
import core.hc_extender as hc_ext
import core.graph as cgraph
import core.gabor as cgabor
from sfcpy import hilbert as hc

img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_11.tif'


if __name__ == '__main__':
    img_block = im.getImage(img_path, display=False)
    hc_index = hc_ext.get_hc_multi_index()
    reduces_block = im.multiPyrDown(img_block[1])[::-1]
    transformed_block = hc_ext.transform(reduces_block, hc_index)

    cgraph.grid_plot(transformed_block, 3, title='HC-Analysis')
    cgraph.grid_plot(reduces_block, 3, is_img=True, title='Images')

    # gabor_set = cgabor.getKernel(20, 20)
    # cgraph.grid_plot2(gabor_set, 9, 'Gabor Jets')
    # gabor_plot = []

    # for i in np.arange(0, len(gabor_set)):
    #     garbor_img = cv2.filter2D(img_block[2], -1, gabor_set[i])
    #     gabor_plot.append(garbor_img)

    # cgraph.grid_plot2(gabor_plot, 3, 'Gabor index: '+str(gabor_index))
    plt.show()
