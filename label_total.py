import numpy as np
import cv2


def labels_total(n_grid_cells, label):

    l_total = []
    x = 640 / n_grid_cells
    y = 480 / n_grid_cells


    for j in range(n_grid_cells):
        for i in range(n_grid_cells):

            dx1 = (j) * x
            dy1 = (i) * y
            dx2 = (j+1) * x
            dy2 = (i+1) * y


            for k in range(len(label)):

                a = label[k]

                if a[1] > dx1 and a[1] < dx2 and a[2] > dy1 and a[2] < dy2:
                    l_total.append(a)

                else:
                    b = [0, 0, 0, 0, 0, 0, 0, 0]
                    l_total.append(b)


    return l_total
