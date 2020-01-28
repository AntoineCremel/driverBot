#!/usr/bin/python3.7

import image_load
import model
import os

def save_model(model):
	json_arch = model.to_json()
	json_path = os.path.join("model", "architecture.json")
	with open(json_path, 'w') as arch_file:
		arch_file.write(json_arch)

	model_path = os.path.join("model", "weights.h5")
	model.save_weights(model_path)

def train(dir_name="lane_images"):
	print("Loading images...")
	images, labels = image_load.read_training(format_size=(64, 64), dir_name=dir_name)
	
	X = image_load.format_X(images, [64, 64])
	Y = image_load.format_Y(labels)

	print("Training model...")
	cnn = model.SmallModel(input_shape=(64, 64, 3))
	cnn.fit(X, Y)
	cnn.summary()

	print("Saving...")
	save_model(cnn)
	

train()