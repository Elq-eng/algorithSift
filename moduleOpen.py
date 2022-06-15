import cv2
import pyautogui
import matplotlib.pyplot as plt
import matplotlib
import pathlib
#para que se muestren d en una carpeta  se debe instalar tkinter y se hace sudo pacman -S tk
matplotlib.use('TkAgg')


# -------------------------------variables globales

#ruta actual de donde se encuentra ejecutandose el proyecto
ruta = pathlib.Path(__file__).parent.absolute()

# Capturar pantalla.
screenshot = pyautogui.screenshot()


# -------------------------------funcion secundaria
def identificationButton(nameImage,imageSection):

    img = cv2.imread(str(ruta) + "/" + nameImage)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # imagen que debe encontrar dentro de la temporal
    img2 = cv2.imread(str(ruta) + "/Images/adicionarNota/"+ imageSection)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    # "busqueda dentro del cromatico"
    method = cv2.TM_CCOEFF
    result = cv2.matchTemplate(img, img2, method)

    # "posiciones del button"
    val_min, val_max, pos_min, pos_max = cv2.minMaxLoc(result)
    higth, width, colors = img2.shape

    # "rectangulo"
    topLeft = pos_max
    buttonRigth = (pos_max[0] + int(width), pos_max[1] + int(higth))

    coordenadas = [pos_max[0] + int(width/2), pos_max[1] + int(higth/2)]

    # "creacion del rectangulo"
    cv2.rectangle(img, topLeft, buttonRigth, (255, 0, 0), 8)

    figure = plt.figure(figsize=(15,15))
    canvas = figure.add_subplot(111)
    canvas.imshow(img)
    plt.show()

    return coordenadas



#funcion de verificacion de ventana
def verifitionTitule(nameImageTemp, imageTitle):
    "imagen escritorio"
    img = cv2.imread(str(ruta) + "/" + nameImageTemp)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    "imagen a encontrar"
    img2 = cv2.imread(str(ruta) + "/Images/adicionarNota/" + imageTitle)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    # sift deteccion de imagenes por caracteres
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # diccionario
    index = dict(algorithm=0, trees=5)

    # busquedad de puntos
    search = dict(checks=50)

    # encontrar el Flann -- "Fast Library for Approximate Nearest Neighbors", libreria que sirve para encontrar un emparejamiento
    # entre los vecinos mas cercanos y aproximados
    flan = cv2.FlannBasedMatcher(index, search)

    # encontrar el mejor emparejamiento entre puntos por descritores o caracteristicas encontradas por el algoritmo sift, parametros
    # descritor 1 y 2, y luego el numero de consultas por emparejamiento por cada punto descrito
    matches = flan.knnMatch(des1, des2, k=2)

    # encontrar los que tengan menor distancia
    best = []
    for e1, e2 in matches:
        if e1.distance < 0.1 * e2.distance:
            best.append([e1])

    print("numero de emparejamientos", len(best))


    # dibujar emparejamiento
    imageMatch = cv2.drawMatchesKnn(img,kp1,img2,kp2,best[0:200], None, flags =0)
    imageMatch = cv2.cvtColor(imageMatch, cv2.COLOR_BGR2RGB)
    plt.imshow(imageMatch)
    plt.show()

    return len(best)



# -------------------------------funcion principal
#definir funcion para identificar secciones de la pantalla
def main():
    # entrada de imagenes
    nameImageTemp = "temp.png"
    imageTitle = "titulo.png"
    imageSection = "guardar.png"

    # toman pantallazo
    screenshot.save(nameImageTemp)

    # verificacion de que si este en la imagen
    validation = verifitionTitule(nameImageTemp, imageTitle)

    #funcion de opencv
    if validation != 0:
        coordenadas = identificationButton(nameImageTemp,imageSection)
        print("coordenada del punto click ",coordenadas)




main()

# consulta de si esta el usuario

