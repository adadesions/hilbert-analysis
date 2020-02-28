import cv2

img_path = 'data/yes/Y1.jpg'
img = cv2.imread(img_path)
cv2.imshow('Img', img)
cv2.waitKey()