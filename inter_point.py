import cv2
import json


def get_pos(event, x, y, flags, param):
    global count, tape

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

        count = count + 1
        point = (x, y)

        print('Label:', cur_labels, '\nCount:', count)
        print(point)

        tape[cur_labels].append(point)


img_name = 'Y1.jpg'
img_path = 'data/yes/'+img_name
img = cv2.imread(img_path)
count = 0
pointer = 0
labels = ['background', 'brain', 'tumor']
cur_labels = labels[pointer]
tape = {
    'file_path': img_path,
    'background': [],
    'brain': [],
    'tumor': []
}



# Resize
# scale_percent = 160 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.namedWindow('image')
cv2.setMouseCallback('image', get_pos)


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(20) & 0xFF

    if k == 27:
        with open('training_points/'+img_name+'.json', 'w') as outfile:
            json.dump(tape, outfile)

        print(tape)
        break
    elif k == ord('c'):
        count = 0
        pointer += 1
        cur_labels = labels[pointer]
