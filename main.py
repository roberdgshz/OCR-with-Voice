import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

cuadro = 100
ancho_camara, alto_camara = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, ancho_camara)
cap.set(4, alto_camara)

def text(image):
    def voz(archi_text, lenguaje, nom_archi):
        with open(nom_archi,"r") as lec:
            lectura = lec.read()
        lect = gTTS(text=lectura, lang=lenguaje, slow=False)
        nombre = nom_archi
        lect.save(nombre)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texto = pytesseract.image_to_string(gris)
    print(texto)
    dire = open('Info.txt', "w")
    dire.write(texto)
    voz("Info.txt", "es", "Voz.mp3")
    audio = 'Voz.mp3'
    playsound(audio)

while True:
    ret, frame = cap.read()
    if ret==False: break
    cv2.putText(frame, 'Coloque el texto aquí:', (158, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0), 2)
    cv2.putText(frame, 'Coloque el texto aquí:', (160, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 0, 0), 2)
    cv2.rectangle(frame, (cuadro, cuadro), (ancho_camara - cuadro, alto_camara - cuadro), (0, 0, 0), 2)
    x1, y1 = cuadro, cuadro
    ancho, alto = (ancho_camara - cuadro) - x1, (alto_camara - cuadro) - y1
    x2, y2 = x1 + ancho, y1 + alto
    doc = frame[y1:y2, x1:x2]
    cv2.imwrite("Image.jpg", doc)

    cv2.imshow("Lector Inteligente", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break

    text(doc)
    cap.release()
    cv2.destroyAllWindows()