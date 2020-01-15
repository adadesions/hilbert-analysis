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
    # hc_index = hc_ext.get_hc_multi_index()
    reduces_block = im.multiPyrDown(img_block[1])[::-1]
    # transformed_block = hc_ext.transform(reduces_block, hc_index)

    # cgraph.grid_plot(transformed_block, 3, title='HC-Analysis')
    # cgraph.grid_plot(reduces_block, 3, is_img=True, title='Images')

    # Gabor Configurations
    # _scales [61, 33, 13, 9]
    gabor_plot = []
    isPlotGabor = True
    _scale = 13
    _resolution, _resIndex = 8, -6

    gabor_set = cgabor.getKernel(_scale)

    if isPlotGabor:
        cgraph.grid_plot2(gabor_set, 8, 7, 'Gabor Jets, scale:{}'.format(_scale))

    for i in np.arange(0, len(gabor_set)):
        garbor_img = cv2.filter2D(reduces_block[_resIndex], -1, gabor_set[i])
        gabor_plot.append(garbor_img)

    cgraph.grid_plot2(gabor_plot, 8, 7, 'Gabor Feature, scale:{}, res:{}'.format(_scale, _resolution))
    plt.show()
