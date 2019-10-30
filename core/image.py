import cv2


def getInfo(imgs, img_path):
    print('Image Information')
    print('==================')
    print('Path:', img_path)

    try:
        for img in imgs:
            print('shape: {} size:{}'.format(img.shape, img.size))
    except TypeError:
        print('ERROR: TypeError, please check function input')


def getImage(img_path, display=True):
    img = cv2.imread(img_path)
    b, g, r = cv2.split(img)
    image_block = [img, b, g, r]

    if display:
        getInfo(image_block, img_path)

        cv2.imshow('Brain', img)
        cv2.imshow('B channel', b)
        cv2.imshow('G channel', g)
        cv2.imshow('R channel', r)

        cv2.waitKey()

    return image_block 


def multiPyrDown(img, debug=False):
    result = [img]
    temp_img = img.copy()

    while temp_img.size > 4:
        if debug:
            print(temp_img.size)
        temp_img = cv2.pyrDown(temp_img)
        result.append(temp_img)

    print('### Multi-PyrDown, Done with length: {} ###'.format(len(result)))

    return result
