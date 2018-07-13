import cv2
import numpy as np


## "/home/aaguerreberry/BASE_DE_DATOS_WBC/BCCD_Dataset/BCCD/JPEGImages/BloodImage_00002.jpg"

path = "/home/aaguerreberry/BASE_DE_DATOS_WBC/BCCD_Dataset/BCCD/JPEGImages/BloodImage_00056.jpg"

img = cv2.imread(path)


def grid_cells(img, n_grid_cells):

    x = img.shape[1] / n_grid_cells

    y = img.shape[0] / n_grid_cells

    image = []

    for j in range(n_grid_cells):
        for i in range(n_grid_cells):

            image.append(img[x*j:x*(j+1), y*i:y*(i+1), :])

            cv2.rectangle(img, (x*j,y*i), (x*(j+1),y*(i+1)), (255, 0, 0), 1)


    return np.asarray(image)

new_image = grid_cells(img, 12)


print(img.shape)
print(new_image.shape)
print(new_image[0].shape)

cv2.imshow("Imagen Original", img)
cv2.imwrite("prueba1.jpg", img)

cv2.waitKey(0)





