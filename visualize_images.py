import cv2
import numpy as np

img = cv2.imread("/home/aaguerreberry/BASE_DE_DATOS_WBC/wbc-classification/Original_Images/BloodImage_00005.jpg")


def grid_cells(img, n_grid_cells):

    x = img.shape[1] / n_grid_cells

    y = img.shape[0] / n_grid_cells

    image = []

    for j in range(n_grid_cells):
        for i in range(n_grid_cells):

            image.append(img[y*j:y*(j+1), x*i:x*(i+1), :])

            cv2.rectangle(img, (y*j,y*(j+1)), (x*i,x*(i+1)), (255, 0, 0), 1)


    return np.asarray(image)

new_image = grid_cells(img, 20)

test = new_image[0]

print(new_image.shape)
print(test.shape)

cv2.imshow("Imagen Original", img)
cv2.imwrite("prueba.jpg", img)



cv2.waitKey(0)



