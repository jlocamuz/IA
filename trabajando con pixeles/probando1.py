#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('./imagenes/7A59104.jpeg')

print(type(img))
img1 = list(img)
# tamano imagen? 

altura = len(img)
ancho = len(img[0])

contador = 0

#altura
# contador = 96
for indice_altura, i in enumerate(img1):
    # ancho 
    # contador = 80
    for indice_ancho, j in enumerate(i):
        print(j[0])
        print(img1[indice_altura][indice_ancho])
        img1[indice_altura][indice_ancho] = (img1[indice_altura][indice_ancho])[0]

cv2.imshow('Original', img)

#borramos parte izquierda
img[0:96, 0:15] = (255, 255, 255)
#borramos parte derecha
img[0:96, -15:] = (255, 255, 255)

#eliminamos arriba
img[0:25, 0:80] = (255, 255, 255)
#eliminamos abajo
img[75:, 0:80] = (255, 255, 255)

cv2.imshow('Original', img)
print('ultimo' , img1[95][79])
print(type(img1))
cv2.imwrite('./modificadas/modificada.jpg',img)
cv2.destroyAllWindows()
