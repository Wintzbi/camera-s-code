import cv2
import pyautogui
import pygetwindow
from PIL import Image
import time
from datetime import datetime
import threading

def screen(time):
    try:
        window = pygetwindow.getWindowsWithTitle('frame')[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        screenshot_path = r'C:\Users\Leynaïck\Desktop\Spé\Projet\Screenshots\\'
        screenshot_path = screenshot_path + time + ".png"
        pyautogui.screenshot(screenshot_path)
        im = Image.open(screenshot_path)
        im = im.crop((left + 10, top + 50, right - 10, bottom - 10))
        cropped_path = r'C:\Users\Leynaïck\Desktop\Spé\Projet\Screenshots\\'
        cropped_path = cropped_path + time + ".png"  
        im.save(cropped_path)
        im.close()
    except IndexError:
        print("La fenêtre 'frame' n'a pas été trouvée.")

def capture_screen(time):
    threading.Thread(target=screen, args=(time,)).start() 

current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(current_time_right_format+'.avi', fourcc, 25.0, (640, 480))

fps_start_time = time.time()
fps_counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        out.write(frame)
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # corrected the time format
        current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('frame', frame)
        
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('m'):
            capture_screen(current_time_right_format)  # Appel de la fonction capture_screen() pour capturer l'écran dans un thread séparé
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()





