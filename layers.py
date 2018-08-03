## construction of layers

import tensorflow as tf


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.5,  name="Weights")
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape, name="bias")
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")


## aplicacion algoritmo non-max supression



def non_max_supression(pc, label, n):

    for k in range(n*n):
        a = label[k]

        if a[0] > pc:
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










