import Image
import numpy as np
import matplotlib
import csv
import sklearn


n_imag = 2411



## opening images...
data = []

path = "000"

for i in range(n_imag):

    path1 = int(path)
    path1 += 1
    path2 = str(path1)

    image = Image.open("/home/aaguerreberry/BASE_DE_DATOS_WBC/wbc-classification/Original_Images/BloodImage_0000" + path2 + ".jpg")
    imarray = np.array(image)
    data.append(imarray)
    path2 = path

data_array = np.asarray(data)
image = data_array.reshape(n_imag, 3, 480, 640)




## opening labels..

path = "/home/aaguerreberry/BASE_DE_DATOS_WBC//wbc-classification/labels.csv"

labels = []
with open(path) as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:



        a = row[1:8]
        labels.append(row[1:8])


labels_array = np.asarray(labels)

new_labels = labels_array[1:, 1]


data = []

for i in range(len(new_labels)):
    if new_labels[i] == 'NEUTROPHIL':
        a = np.array([0, 0, 0, 0, 0, 1])
        b = a.tolist()
        data.append(b)

    elif new_labels[i] == 'BASOPHIL':
        a = np.array([0, 0, 0, 0, 1, 0])
        b = a.tolist()
        data.append(b)

    elif new_labels[i] == 'EOSINOPHIL':
        a = np.array([0, 0, 0, 1, 0, 0])
        b = a.tolist()
        data.append(b)

    elif new_labels[i] == 'LYMPHOCYTE':
        a = np.array([0, 0, 1, 0, 0, 0])
        b = a.tolist()
        data.append(b)

    elif new_labels[i] == 'MONOCYTE':
        a = np.array([0, 1, 0, 0, 0, 0])
        b = a.tolist()
        data.append(b)

    else:
        a = np.array([1])
        b = a.tolist()
        data.append(b)



# remueve las imagenes que tienen mas de un nucleo
def remover_masdeun_nucleo(n_imag, imagen, data):
    """
    :return: a: imagenes con solo 1 nulceo
             b: los respectivos labels
    """

    contador = 0
    for i in range(n_imag):
        if i == 10 or i == 31 or i == 34 or i == 43 or i == 44 or i == 65 or i == 70 or i == 134 or i == 176 or i == 193 or i == 195 or i == 233 or i == 242 or i == 249:

            imagen = np.delete(imagen, (i - contador), 0)
            data = np.delete(data, (i - contador), 0)
            contador += 1
    return imagen, data, contador


# remueve las imagenes que no estan identificadas
def remover_no_indetificadas(n_imag, imagen, data, contador):
    aux = imagen
    cont = 0
    for i in range(n_imag - contador):
        if data[i] == [1]:

            aux = np.delete(aux, (i - cont), 0)
            cont += 1

    return aux

a, b, contador = remover_masdeun_nucleo(n_imag, image, data)
prueba = remover_no_indetificadas(n_imag, a, b, contador)


print(image.shape)
print(a.shape)
print(prueba.shape)


