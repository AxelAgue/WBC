import cv2

img = cv2.imread("/home/aaguerreberry/BASE_DE_DATOS_WBC/wbc-classification/Original_Images/BloodImage_00005.jpg")

cv2.imshow("Imagen Original", img)

## Funciones para preporcesar las imagenes:




## para rotar las imagenes
def rotate_images(image, angle):
    (h, w) = image.shape[:2]
    medio = (w/2, h/2)

    M = cv2.getRotationMatrix2D(medio, angle, 1.0)
    imagen_rotada = cv2.warpAffine(image, M, (w, h))
    return imagen_rotada

## para invertir las imagenes
def flip_images(image):
    h_img = image.copy()
    v_img = image.copy()
    h_img = cv2.flip(image, 0)
    v_img = cv2.flip(image, 1)
    return h_img, v_img


img_rotada1 = rotate_images(img, angle=90)
cv2.imshow("Rotada_90", img_rotada1)

img_rotada2 = rotate_images(img, angle=180)
cv2.imshow("Rotada_180", img_rotada2)

img_rotada3 = rotate_images(img, angle=270)
cv2.imshow("Rotada_270", img_rotada3)


h_img1, v_img1 = flip_images(img_rotada1)
h_img2, v_img2 = flip_images(img_rotada2)
h_img3, v_img3 = flip_images(img_rotada3)



cv2.imshow( "Rotada_90_Horizontal flip1", h_img1 )
cv2.imshow( "Rotada_90_Vertical flip1", v_img1 )

cv2.imshow( "Rotada_180_Horizontal flip2", h_img2 )
cv2.imshow( "Rotada_180_Vertical flip2", v_img2 )

cv2.imshow( "Rotada_270_Horizontal flip3", h_img3 )
cv2.imshow( "Rotada_270_Vertical flip3", v_img3 )

cv2.waitKey(0)





# para reducir las dimensiones... (max_pooling)
def max_pool(image, kernel_size, stride):
    C, H, W = image.shape
    S = stride
    H_P = kernel_size
    W_P = kernel_size

    HH = 1 + (H - H_P) / S
    WH = 1 + (W - W_P) / S

    output = np.zeros((C, HH, WH))

    for depth in xrange(C):
        for r in xrange(0,H,S):
            for c in xrange(0,W,S):
                output[depth,r/S,c/S] = np.max(image[depth,r:r+H_P,c:c+W_P])

    return output

# para normlizar iamgenes...
def normalize(image):
    C, H, W = image.shape
    mascara = np.ones((C, H, W)) * 255
    imagen_normalizada = image / mascara

    return imagen_normalizada



