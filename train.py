#!/usr/bin/python3

import image_load
import model

def train(dir_name="lane_images"):
	images, labels = image_load.read_training(format_size=(64, 64), dir_name=dir_name)
	
	X = image_load.format_X(images, [64, 64])
	Y = image_load.format_Y(labels)

	cnn = model.SmallModel(input_shape=(64, 64, 3))
	cnn.fit(X, Y)
	cnn.summary()

train()