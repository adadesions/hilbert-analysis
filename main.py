import cv2
import numpy as np
import matplotlib.pyplot as plt
import core.image as im
import core.hc_extender as hc_ext
from sfcpy import hilbert as hc

img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_11.tif'


def grid_plot(data, size, title='Untitle', is_img=False):
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    length = size**2
    iter_data = data if is_img else data.values()
    graphs = []

    for i in range(1, length+1):
        temp_plt = fig.add_subplot(''.join([str(size)*2, str(i)]))
        graphs.append(temp_plt)

    for i, d in enumerate(iter_data):
        if is_img:
            graphs[i].imshow(d, cmap=plt.cm.gray)
        else:
            graphs[i].plot(d)


if __name__ == '__main__':
    img_block = im.getImage(img_path, display=False)
    hc_index = hc_ext.get_hc_multi_index()
    reduces_block = im.multiPyrDown(img_block[3])[::-1]
    transformed_block = hc_ext.transform(reduces_block, hc_index)

    grid_plot(transformed_block, 3, title='HC-Analysis')
    grid_plot(reduces_block, 3, is_img=True, title='Images')
    plt.show()
