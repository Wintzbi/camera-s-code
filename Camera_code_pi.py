import time
from picamera2 import Picamera2, Preview

# Création de l'instance PiCamera2
picam = Picamera2()
types = True

# Configuration de l'aperçu
config = picam.create_preview_configuration()
picam.configure(config)

# Démarrage de l'aperçu
picam.start_preview(Preview.QTGL)

def take_screenshot():
    try:
        # Capture d'une image
        picam.start()
        time.sleep(1)  # Attente pour stabiliser l'image
        picam.capture_file("screenshot.jpg")
    finally:
        # Assurez-vous d'arrêter la capture même en cas d'erreur
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
