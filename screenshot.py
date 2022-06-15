import cv2
import pyautogui
import matplotlib.pyplot as plt
import matplotlib
import pathlib

#ruta actual de donde se encuentra ejecutandose el proyecto
ruta = pathlib.Path(__file__).parent.absolute()


#para que se muestren d en una carpeta  se debe instalar tkinter y se hace sudo pacman -S tk
matplotlib.use('TkAgg')

# Capturar pantalla.
screenshot = pyautogui.screenshot()

# Guardar imagen.
nameImage = "testCoordinate3.png";

screenshot.save(nameImage)
#leer la imagen por opencv
img = cv2.imread(str(ruta) + "/" + nameImage)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"imagen a encontrar"
img2 = cv2.imread(str(ruta) + "/button.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


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

plt.imshow(img)
plt.show()



