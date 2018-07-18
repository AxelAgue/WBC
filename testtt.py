import xml.etree.ElementTree as ET
import cv2
import numpy as np

num_image = "005"

image = cv2.imread(
    "/home/aaguerreberry/BASE_DE_DATOS_WBC/BCCD_Dataset/BCCD/JPEGImages/BloodImage_00" + num_image + ".jpg")

tree = ET.parse(
    "/home/aaguerreberry/BASE_DE_DATOS_WBC/BCCD_Dataset/BCCD/Annotations/BloodImage_00" + num_image + ".xml")


def give_label(tree):
    labels = []

    for elem in tree.iter():

        if 'object' in elem.tag or 'part' in elem.tag:
            for attr in list(elem):

                aux = []

                if 'name' in attr.tag:
                    name = attr.text
                    aux.append([0, 1])

                if 'bndbox' in attr.tag:
                    for dim in list(attr):

                        if 'xmin' in dim.tag:
                            xmin = int(round(float(dim.text)))
                        if 'ymin' in dim.tag:
                            ymin = int(round(float(dim.text)))
                        if 'xmax' in dim.tag:
                            xmax = int(round(float(dim.text)))
                        if 'ymax' in dim.tag:
                            ymax = int(round(float(dim.text)))

                    if name[0] == "R":
                        # presencia de objeto
                        aux.append(1)

                        # dimenisons de la bounding box
                        x = xmin + (xmax - xmin) / 2
                        y = ymin + (ymax - ymin) / 2

                        w = xmax - xmin
                        h = ymax - ymin

                        aux.append(x)
                        aux.append(y)
                        aux.append(w)
                        aux.append(h)

                        # clase a la que pertenece
                        aux.append(0)
                        aux.append(0)
                        aux.append(1)

                    if name[0] == "W":
                        # presencia de objeto
                        aux.append(1)

                        # dimenisons de la bounding box
                        x = xmin + (xmax - xmin) / 2
                        y = ymin + (ymax - ymin) / 2

                        w = xmax - xmin
                        h = ymax - ymin

                        aux.append(x)
                        aux.append(y)
                        aux.append(w)
                        aux.append(h)

                        # clase a la que pertenece
                        aux.append(0)
                        aux.append(1)
                        aux.append(0)

                    if name[0] == "P":
                        # presencia de objeto
                        aux.append(1)

                        # dimenisons de la bounding box
                        x = xmin + (xmax - xmin) / 2
                        y = ymin + (ymax - ymin) / 2

                        w = xmax - xmin
                        h = ymax - ymin

                        aux.append(x)
                        aux.append(y)
                        aux.append(w)
                        aux.append(h)

                        # clase a la que pertenece
                        aux.append(1)
                        aux.append(0)
                        aux.append(0)

            labels.append(aux)
    return np.asarray(labels)


def labels_total(n_grid_cells, label):
    l_total = []
    x = 640 / n_grid_cells
    y = 480 / n_grid_cells

    for j in range(n_grid_cells):
        for i in range(n_grid_cells):

            dx1 = (j) * x
            dy1 = (i) * y
            dx2 = (j + 1) * x
            dy2 = (i + 1) * y

            a = np.asarray([0, 0, 0, 0, 0, 0, 0, 0])

            for k in range(len(label)):


                if label[k][1] > dx1 and label[k][1] < dx2 and label[k][2] > dy1 and label[k][2] < dy2:

                    a = label[k]


            l_total.append(a)

    return np.asarray(l_total)


label_test = give_label(tree)

total = labels_total(10, label_test)

## print(label_test)

print(total)



def plot_from_labels(image, label, n_grid_cells):

    for k in range(n_grid_cells*n_grid_cells):

        aux = label[k]

        if aux[0] == 1:

            bx = aux[1]
            by = aux[2]
            w = aux[3]
            h = aux[4]

            xmin, ymin = bx - w/2, by - h/2

            xmax, ymax = bx + w/2, by + h/2
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)


plot_from_labels(image, total, 10)
## cv2.imshow("Imagen Original", image)
cv2.imwrite("pruebaaa.jpg", image)
cv2.waitKey(0)