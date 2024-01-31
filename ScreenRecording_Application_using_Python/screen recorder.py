# Install the importing modules in the respective environment

import os
os.system("pip install opencv-python")
os.system("pip install pyautogui")
os.system("pip install numpy")
os.system("pip install pywin32")
os.system("pip install win10toast")

#Then importing our modules

import cv2
import pyautogui
from win32.win32api import GetSystemMetrics
import numpy as np
import time
from toast import *

#Notified when app starts
start()

# Then we must set the width and height of our recorder same as your laptop/PC screen

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)

#format can define on how to write the video data in it
frames_per_seconds = 24
format = cv2.VideoWriter_fourcc(*'mp4v')

saved_file = "C:/Users/chara/Desktop/"

# Here we can change the FPS (Frame Per Second in 20 fps)

video_output_data = cv2.VideoWriter("ScreenRecord_20_fps.mp4", format, 20.0, dimension)

# Here we can change the FPS (Frame Per Second in 30 fps)

#video_output_data = cv2.VideoWriter("ScreenRecord_30_fps.mp4", format, 30.0, dimension)

# Here we can change the FPS (Frame Per Second in 60 fps)

#video_output_data = cv2.VideoWriter("ScreenRecord_60_fps.mp4", format, 60.0, dimension)

# Now we must set the time interval for Record the video

Present_time = time.time()
# Take how much time you required in the Duration variable

#Duration = int(input("Enter the duration time to record:"))
Duration = 25

#To stop the recording time we must put finish time in order to stop the recording video

finish_time = Present_time + Duration

while True:
    #   Here pyautogui.screenshot() captured screenshots which merge into a ScreenRecord
    picture = pyautogui.screenshot()
    # Here we store all the screenshots in an array
    frame = np.array(picture)
    # Here we get the original color by using cv2.COLOR_BGR2RGB
    frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Now we store the video output here
    video_output_data.write(frame_1)
    # Now check the duration
    current_time = time.time()
    if current_time > finish_time:
        break
# Finally release your ScreenRecord
video_output_data.release()
cv2.destroyAllWindows()


#Notify when app stops
stop()

#Shows the file path in which the recorded video can also saved at same path

file_path = os.path.dirname(os.path.abspath(__file__))
filesaved_path(file_path)