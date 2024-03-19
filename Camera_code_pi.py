import time
from picamera2 import PiCamera2, Preview

# Création de l'instance PiCamera2
picam = PiCamera2()
types = True

# Configuration de l'aperçu
config = picam.create_preview_configuration()
picam.configure(config)

# Démarrage de l'aperçu
picam.start_preview(Preview.QTGL)

try:
    while types:
        picam.start()
        time.sleep(5)
        # Détecter la pression de la touche "Q"
        if input("Appuyez sur 'Q' pour arrêter : ").lower() == 'q':
            types = False
        picam.capture_file("test-python.jpg")
finally:
    # Fermeture de la caméra
    picam.close()
