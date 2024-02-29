# importamos las librerias
import cv2

# lectura de la imagen
imagen = cv2. imread('img.png')

# rotacion 1
rot1 = cv2. flip(imagen, 0)

# rotacion 2
rot2 = cv2.flip(imagen, 1)

# rotacion 3
rot3 = cv2.flip(imagen, -1)

# ploteamos los cambios:
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('ROTACION 1', rot1)
cv2.imshow('ROTACION 2', rot2)
cv2.imshow('ROTACION 3', rot3)

cv2.waitKey(0)

