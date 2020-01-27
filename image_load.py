#!/usr/bin/python3

import json
import numpy as np
from os import path
from PIL import Image, ImageEnhance

def read_training(format_size=(16, 16), dir_name="lane_images", label_file="labels.json", extrapolate=True):
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

	image_list = []
	label_list = []
	for image_name, label in labels.items():
		# First open the image in the right format
		image_file_name = path.join(dir_name, image_name)
		image = Image.open(image_file_name).resize(format_size)
		image_list.append(list(image.getdata()))
		label_list.append(label)

		if extrapolate:
			mirror_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
			image_list.append(list(mirror_image.getdata()))
			if label == 'B' or label == 'F':
				label_list.append(label)
			elif label == 'L':
				label_list.append('R')
			elif label == 'R':
				label_list.append('L')
			else:
				raise Exception("Label unknown")

	return np.array(image_list), np.array(label_list)

def format_X(image_list, format):
	image_list = image_list.reshape(image_list.shape[0], format[0], format[1], image_list.shape[2])
	return image_list/255

def label_to_cat(label):
	if label == 'F':
		return [1, 0, 0, 0]
	if label == 'R':
		return [0, 1, 0, 0]
	if label == 'L':
			return [0, 0, 1, 0]
	if label == 'B':
		return [0, 0, 0, 1]
		
	raise Exception("Label unknown")

def format_Y(label_list):
	"""
	In order to be compatible with a neural network, the labels need to be converted to
	categorical data.
	"""
	categorical_y = []
	for label in label_list:
		categorical_y.append(label_to_cat(label))

	return np.array(categorical_y)