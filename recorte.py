# Importación de librerías:
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creamos el "canvas" de trabajo o matriz principal:
img = 100 * np.ones((10, 10, 3), np.uint8)
# img2 = 100 * np.ones((10, 10, 3), np.uint8)

# Vanos a modificar una porción de la imagen a recortar
# modificamos el pixel (4, 5) del canal R
img[4, 5, 0] = 255
img[4, 4, 0] = 0
img[5, 4, 0] = 255
img[5, 5, 0] = 0

# modificamos el pixel (4, 5) del canal G
img[4, 5, 1] = 0
img[4, 4, 1] = 255
img[5, 4, 1] = 0
img[5, 5, 1] = 255

# Modificamos ls pxeles de la matriz B
img[4, 5, 2] = 255
img[4, 4, 2] = 255
img[5, 4, 2] = 0
img[5, 5, 2] = 0

# Hacemos el recorte
recorte = img[3:7, 3:7]

# Ploteamos los canales:
fig = plt.figure()

# Imagen original:
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img)
ax1.set_title("IMAGEN")

# el recorte
ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img)
ax2.set_title("RECORTE")

plt.show()

# Ahora trataremos una magen
# leemos laimagen
imagen = cv2.imread('iron_man.jpg')

# recortamos una porcion
recorte_imagen = imagen[126:570, 400:734]

# Ploteamos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('RECORTE', recorte_imagen)

cv2.waitKey(0)

