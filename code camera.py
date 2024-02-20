import cv2
import pyautogui
import pygetwindow
from PIL import Image
import time
from datetime import datetime
import threading

# Function to capture a screenshot of a specific window and save it
def screen(time): 
    try:
        # Get the window titled 'frame'
        window = pygetwindow.getWindowsWithTitle('frame')[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        
        # Define the path to save the screenshot
        screenshot_path = r'C:\Users\Leynaïck\Desktop\Spé\Projet\Screenshots\\'
        screenshot_path = screenshot_path + time + ".png"
        
        # Take a screenshot and save it
        pyautogui.screenshot(screenshot_path)
        
        # Open the screenshot using PIL
        im = Image.open(screenshot_path)
        
        # Crop the image to exclude borders
        im = im.crop((left + 10, top + 50, right - 10, bottom - 10))
        
        # Define the path to save the cropped image
        cropped_path = r'C:\Users\Leynaïck\Desktop\Spé\Projet\Screenshots\\'
        cropped_path = cropped_path + time + ".png"  
        
        # Save the cropped image
        im.save(cropped_path)
        im.close()
    except IndexError:
        print("The window 'frame' was not found.")

# Function to capture the screen in a separate thread
def capture_screen(time): 
    threading.Thread(target=screen, args=(time,)).start() 

# Get the current time in the right format
current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(current_time_right_format+'.avi', fourcc, 25.0, (640, 480))

# Variables for FPS calculation
fps_start_time = time.time()
fps_counter = 0

# Main loop to capture video frames
while cap.isOpened():
    # Read a frame from the video capture
    ret, frame = cap.read()
    if ret:
        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        
        # Write the frame to the output video
        out.write(frame)
        
        # Get the current time and format it
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_time_right_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Put the current time on the frame
        cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the frame in a window titled 'frame'
        cv2.imshow('frame', frame)
        
        # Wait for a key press
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('m'):
            # If 'm' is pressed, capture the screen
            capture_screen(current_time_right_format)
    else:
        break

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
