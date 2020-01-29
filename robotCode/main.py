#!/usr/bin/python
import RPi.GPIO as GPIO 
import os
import sys

from threading import Timer,Thread, Event

from motor import Motor
from camera import Camera

class Periodic_Thread():
    def __init__(self, t, function):
        self.t=t
        self.function = function
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.function()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
	self.thread.cancel()

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Creation des objets motor et camera
robot_motor = Motor()
robot_camera = Camera()

robot_camera.width = 1280
robot_camera.height = 720
robot_camera.path = '/home/pi/python/PFE_Autonomous_Robot/camera_images/'

#Initialistion des objets motor et camera
robot_motor.motor_init()
robot_camera.camera_init()

#Creation des threads
thread_camera = Periodic_Thread(0.001, robot_camera.camera_capturing_image) 
thread_motor = Periodic_Thread(0.001, robot_motor.left)

#Lancement des threads
thread_camera.start()
thread_motor.start()

#Attend que les threads se terminent
#thread_camera.join()
#thread_motor.join()
