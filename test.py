import cv2
import numpy as np

img = cv2.imread("/home/aaguerreberry/BASE_DE_DATOS_WBC/wbc-classification/Original_Images/BloodImage_00005.jpg")

n_grid_cells = 20

x = img.shape[1] / n_grid_cells
y = img.shape[0] / n_grid_cells

data = []

a = img[y*0:y*(0+1), x*0:x*(0+1), :]
data.append(a)

cv2.rectangle(img, (y*0, y*0), (x*(0+1), x*(0+1)), (255, 0, 0), 1)

b = img[y*1:y*(1+1), x*1:x*(1+1), :]
data.append(b)

cv2.rectangle(img, (y*1, y*0), (x*(1+1), x*(0+1)), (255, 0, 0), 1)

dd = np.asarray(data)


cv2.imshow("Imagen Original", img)
cv2.imwrite("prueba.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()