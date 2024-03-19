import time
import cv2
from picamera2 import PiCamera2, Preview

# Création de l'instance PiCamera2
picam = PiCamera2()
types = True

# Configuration de l'aperçu
config = picam.create_preview_configuration()
picam.configure(config)

# Démarrage de l'aperçu
picam.start_preview(Preview.QTGL)

def take_screenshot():
    # Capture d'une image
    picam.start()
    picam.capture_file("screenshot.jpg")
    picam.stop()  # Arrêt de la capture

try:
    while types:
        # Détecter la pression de la touche "Q" ou "m"
        key = input("Appuyez sur 'Q' pour arrêter, ou 'm' pour prendre un screenshot : ").lower()
        if key == 'q':
            types = False
        elif key == 'm':
            take_screenshot()
finally:
    # Fermeture de la caméra
    picam.close()
