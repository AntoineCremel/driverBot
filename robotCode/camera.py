
import RPi.GPIO as GPIO
import time
import os
import sys

import pygame
import pygame.camera
from pygame.locals import *

from datetime import datetime

class Camera:
	def __init__(self):
		# Attributs
		self.width = ""
		self.height = ""
		self.path = ""
		self.cam_ID = ""
		self.camera = ""

	def camera_init(self):
		#Initialize the time
		now = datetime.now()

		#Initialize pygame
		pygame.init()
		pygame.camera.init()
		cam_list = pygame.camera.list_cameras()
		self.cam_ID = cam_list[0]
		self.camera = pygame.camera.Camera(self.cam_ID,(self.width, self.height))
		self.camera.start()

	def camera_capturing_image(self):
		image = self.camera.get_image()
		#File name for the picture
		now = datetime.now()
		current_time = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
		filename = self.path + current_time + ".jpg"
			#print (filename)
		#Saving the image
		pygame.image.save(image,filename)

