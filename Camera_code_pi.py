import time
from picamera2 import Picamera2, Preview

picam = Picamera2()
types = True

config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)
while types:
        picam.start()
        time.sleep(5)
        types = False
        picam.capture_file("test-python.jpg")

picam.close()
