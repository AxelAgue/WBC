


def non_max_supression(label):
    for k in range(2):
        a = label[k]

        if a[0] < 0.6:
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 0
            a[4] = 0
            a[5] = 0
            a[6] = 0
            a[7] = 0

    label[k] = a

    return label


"""
label = [[0.7, 0, 0, 4, 6, 7, 8, 8], [0.2, 0, 0, 4, 6, 7, 8, 8]]
sss = non_max_supression(label)
print(sss)
"""

## graficar salida


