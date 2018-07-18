"""
Implementacion del algoritmo YOLO en Tensorflow.

Localizacion de C Sanguineas en Imagenes Microcopicas.

"""

import tensorflow as tf

def loss_function(original_label, yolo_label, n_grid_cells):

    ## uso mismos valores que el paper

    l_noobj = 5.0
    l_coord = 0.5

    p_hat = []
    x_hat = []
    y_hat = []
    w_hat = []
    h_hat = []
    c1_hat = []
    c2_hat = []
    c3_hat = []

    for k in range(n_grid_cells*n_grid_cells):

        aux = yolo_label[k]

        p_hat.append = aux[0]
        x_hat.append = aux[1]
        y_hat.append = aux[2]
        w_hat.append = aux[3]
        h_hat.append = aux[4]
        c1_hat.append = aux[5]
        c2_hat.append = aux[6]
        c3_hat.append = aux[7]


    p = []
    x = []
    y = []
    w = []
    h = []
    c1 = []
    c2 = []
    c3 = []

    for k in range(n_grid_cells*n_grid_cells):

        aux2 = original_label[k]

        p.append = aux2[0]
        x.append = aux2[1]
        y.append = aux2[2]
        w.append = aux2[3]
        h.append = aux2[4]
        c1.append = aux2[5]
        c2.append = aux2[6]
        c3.append = aux2[7]


    x_err = tf.square(x - x_hat)
    y_err = tf.square(y - y_hat)
    w_err = tf.square(tf.sqrt(w) - tf.sqrt(w_hat))
    h_err = tf.square(tf.sqrt(h) - tf.sqrt(h_hat))
    c1_err = tf.square(c1 - c1_hat)
    c2_err = tf.square(c2 - c2_hat)
    c3_err = tf.square(c3 - c3_hat)
    p_err = tf.square(p - p_hat)

    loss = tf.reduce_sum(

        tf.reduce_sum(
             (
                l_coord * (x_err + y_err + w_err + h_err)
                + c1_err + c2_err + c3_err + p_err
            )

    ))

    return loss






