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
    transformed = {}

    for idx, img in enumerate(reduces_block):
        order = idx+1
        mapping = hc_order[str(order)]
        transformed[str(order)] = []
        for point in mapping:
            x, y = point[0], point[1]
            transformed[str(order)].append(img[x, y])
            # print('ok')
    
    print(transformed)
