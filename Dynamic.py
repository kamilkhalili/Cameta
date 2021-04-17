from picamera import PICamera
from time import sleep
import datetime

camera = PiCamera()

camera.start_preview()                                     #Start camera
sleep(5)                                                   #Allow camera to calibrate
date=datetime.datetime.now()strftime("%m_%d_%Y_%H_%M_%S")  #Check time and date  
camera.capture("/home/pi/photobooth/"+ date + ".jpg")      #Capture photo  
camera.stop_preview()                                      #Stop camera
