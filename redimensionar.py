# importamos las librerías
import cv2

# lectura de la imágen:
imagen = cv2.imread('img.png')

# redimensionamiento de la imagen, estructura:
# red = cv2.resize(img, outimg, fx, fy, interpolation)

# redimensaionamiento 1
redim_1 = cv2.resize(imagen, None, fx=1.5, fy=1.5)

# redimensionamiento 2:
redim_2 = cv2.resize(imagen, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)

# redimensionamiento 3
redim_3 = cv2.resize(imagen, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# REDIMENSIONAMIENTO 4
ancho = 400
alto = 500
tam = (ancho, alto)
redim_4 = cv2.resize(imagen, tam, interpolation=cv2.INTER_CUBIC)

# pLOTEAMOS EL RECORTE
cv2.imshow('IMAGEN ORIGINAL', imagen)
# cv2.imshow('REDIMENSION 1', redim_1)
# cv2.imshow('REDIMENSION 2', redim_2)
# cv2.imshow('REDIMENSION 3', redim_3)
cv2.imshow('REDIMENSION 4', redim_4)

cv2.waitKey(0)
