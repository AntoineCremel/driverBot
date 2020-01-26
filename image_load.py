#!/usr/bin/python3

import json
from os import path
from PIL import Image

"""im = Image.open("lane_images/2020-01-15_07-45-44-394816.jpg")

im.show()"""

def read_training(format_size=(32,32), dir_name="lane_images", label_file="labels.json", extrapolate=True):
	"""
	read_training will go into dir_name and look for a file called 
	labels.json. It will then open all the images named in labels.json
	and convert them to images of size format_size.

	If extrapolate, then each image will be duplicated to its mirror version.
		- The mirrors of images labelled left or right will be labelled with their opposite
		direction
		- The mirrors of images labelled forward or backward will be labelled with the same
		direction.
	"""
	pathname = path.join(dir_name, label_file)
	with open(pathname, 'r') as lab:
		labels = json.load(lab)

	for image_name, label in labels:
		# First open the image in the right format
		image_file_name = path.join(dir_name, image_name)
		image = Image.open(image_file_name).resize(format_size)
		

read_training()