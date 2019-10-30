import cv2
import numpy as np
import matplotlib.pyplot as plt
import core.image as im
import core.hc_extender as hc_ext
import core.graph as cgraph
from sfcpy import hilbert as hc

img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_11.tif'


if __name__ == '__main__':
    img_block = im.getImage(img_path, display=False)
    hc_index = hc_ext.get_hc_multi_index()
    reduces_block = im.multiPyrDown(img_block[1])[::-1]
    transformed_block = hc_ext.transform(reduces_block, hc_index)

    cgraph.grid_plot(transformed_block, 3, title='HC-Analysis')
    cgraph.grid_plot(reduces_block, 3, is_img=True, title='Images')
    plt.show()
