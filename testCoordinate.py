import cv2
import matplotlib.pyplot as plt
import matplotlib
#para que se muestren d en una carpeta  se debe instalar tkinter y se hace sudo pacman -S tk
matplotlib.use('TkAgg')

"imagen escritorio"
img = cv2.imread("/run/media/elquincascavita/games/COS/proyecto4/Images/CNS-CLIENTE/CNS-CLIENTE.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


"imagen a encontrar"
img2 = cv2.imread("/run/media/elquincascavita/games/COS/proyecto4/Images/CNS-CLIENTE/titulo.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


# sift deteccion de imagenes por caracteres
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# diccionario
index = dict(algorithm = 0, trees = 5)


# busquedad de puntos
search = dict(checks=50)

# encontrar el Flann -- "Fast Library for Approximate Nearest Neighbors", libreria que sirve para encontrar un emparejamiento
# entre los vecinos mas cercanos y aproximados
flan = cv2.FlannBasedMatcher(index, search)

# encontrar el mejor emparejamiento entre puntos por descritores o caracteristicas encontradas por el algoritmo sift, parametros
# descritor 1 y 2, y luego el numero de consultas por emparejamiento por cada punto descrito
matches = flan.knnMatch(des1,des2,k=2)

# encontrar los que tengan menor distancia
best = []
for e1,e2 in matches:
    if e1.distance < 0.1*e2.distance:
        best.append([e1])

print(len(best))

# # dibujar emparejamiento
# imageMatch = cv2.drawMatchesKnn(img,kp1,img2,kp2,best[0:200], None, flags =0)
# imageMatch = cv2.cvtColor(imageMatch, cv2.COLOR_BGR2RGB)
# plt.imshow(imageMatch)
# plt.show()

if len(best) != 0:
    "busqueda dentro del cromatico"
    method = cv2.TM_CCOEFF
    result  = cv2.matchTemplate(img,img2,method)

    "posiciones del button"
    val_min, val_max,pos_min, pos_max = cv2.minMaxLoc(result)
    higth, width, colors = img2.shape

    "rectangulo"
    topLeft = pos_max
    buttonRigth = (pos_max[0]+ width, pos_max[1] + higth)

    "creacion del rectangulo"
    cv2.rectangle(img, topLeft, buttonRigth, (255,0,0),8)

    "imagen con deteccion de objeto"
    plt.imshow(img)
    plt.show()


