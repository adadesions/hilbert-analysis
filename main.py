import cv2
import numpy as np
import core.image as im
import core.hc_extender as hc_ext
from sfcpy import hilbert as hc

img_path = 'data/kaggle_3m/TCGA_CS_4941_19960909/TCGA_CS_4941_19960909_11.tif'

if __name__ == '__main__':
    img_block = im.getImage(img_path, display=False)
    hc_order = hc_ext.get_hc_multi_index()
    reduces_block = im.multiPyrDown(img_block[1])[::-1]

    for img in reduces_block:
        print(img.shape)
    
