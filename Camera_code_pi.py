import picamera2
import cv2
import time
import subprocess
from datetime import datetime

# Function to display the captured screenshot
def display_screenshot(image_path):
    try:
        # Utilize subprocess to call the image viewer
        subprocess.run(["feh", "--fullscreen", image_path])
    except Exception as e:
        print("An error occurred while displaying the screenshot:", e)

def capture_screen(current_time): 
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
        current_time_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Put the current time on the frame
        cv2.putText(frame, current_time_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Define the path to save the screenshot
        screenshot_path = "/home/pi/Desktop/Screenshots/"
        screenshot_filename = screenshot_path + current_time_str + ".png"
        
        # Save the frame as a screenshot
        cv2.imwrite(screenshot_filename, frame)
        
        # Display the screenshot
        display_screenshot(screenshot_filename)
    except Exception as e:
        print("An error occurred:", e)

try:
    # Main loop to capture video frames
    while True:
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('m'):
            # If 'm' is pressed, capture the screen
            capture_screen(datetime.now())
        
finally:
    cv2.destroyAllWindows()
