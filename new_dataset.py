import cv2
import numpy as np



img = cv2.imread("C:/Users/axel_/Desktop/Varios/ALL_IDB1/im/Im003_1.jpg")


"""

"""

def divide_images(image):

    img1 = image[0:683, 0:855, :]
    img2 = image[0:683, 856:1711, :]
    img3 = image[684:1367, 0:855, :]
    img4 = image[684:1367, 856:1711, :]


    return img1, img2, img3, img4

"""
img1, img2, img3, img4 = divide_images(img)
cv2.imshow("test1", img1)
cv2.imshow("test2", img2)
cv2.imshow("test3", img3)
cv2.imshow("test4", img4)

cv2.waitKey()
"""



f = open("C:/Users/axel_/Desktop/Varios/ALL_IDB1/xyc/Im003_1.xyc", "r")
a = f.read()
label = np.fromstring(a, dtype=int, sep=' ')

def labels(label):
    aa = []
    len = int(label.shape[0]/ 2)

    for i in range(len):
        aa.append([label[i * 2], label[i * 2 + 1]])

    return aa

def plot_labels(image, label, bb_size):
    for i in range(len(label)):
        aux = label[i]
        x = aux[0]
        y = aux[1]
        ## cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

        xmin = x - bb_size
        xmax = x + bb_size
        ymin = y + bb_size
        ymax = y - bb_size

        cv2.rectangle(image, (xmin, ymin),
                      (xmax, ymax), (0, 0, 255), 1)


label_total = labels(label)
img1, img2, img3, img4 = divide_images(img)
plot_labels(img, label_total, bb_size=60)

cv2.imshow("test.jpg", img)
cv2.imwrite("test.jpg", img)
cv2.waitKey()