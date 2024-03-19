import picamera2
import cv2
import time
import subprocess
from datetime import datetime

# Function to capture a screenshot of a specific window and save it
def display_screenshot(image_path):
    try:
        # Utilisez subprocess pour appeler le visualiseur d'image
        subprocess.run(["feh", "--fullscreen", image_path])
    except Exception as e:
        print("An error occurred while displaying the screenshot:", e)

def capture_screen(time): 
    try:
        # Capture the screen using PiCamera
        with picamera2.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.capture('frame.jpg')
        
        # Read the captured frame using OpenCV
        frame = cv2.imread('frame.jpg')
        
        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        
        # Get the current time and format it
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Put the current time on the frame
        cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Define the path to save the screenshot
        screenshot_path = r'C:\Users\Leynaïck\Desktop\Spé\Projet\Screenshots\\'
        screenshot_path = screenshot_path + time + ".png"
        
        # Save the frame as a screenshot
        cv2.imwrite(screenshot_path, frame)

        display_screenshot(screenshot_path)
    except Exception as e:
        print("An error occurred:", e)

# Get the current time in the right format
current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

try:
    # Main loop to capture video frames
    while True:
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('m'):
            # If 'm' is pressed, capture the screen
            capture_screen(current_time_right_format)
        
finally:
    cv2.destroyAllWindows()
