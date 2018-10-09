# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2
import os
import config

import schedule
import time
import datetime

def job():
    print(str(datetime.datetime.now())+' logged...')

    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(config.path_to_store_screen_shots+str(datetime.datetime.now())+'.png', image)

# schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("10:35").do(job)
schedule.every().day.at("12:30").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("14:45").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("15:30").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("16:30").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("17:30").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("18:30").do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)

