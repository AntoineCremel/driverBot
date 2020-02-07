#!/usr/bin/python3.7

import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization
import image_load

standard_format = (64, 36)
input_shape = standard_format + (3,)

class SmallModel(Sequential):
	def __init__(self, input_shape=input_shape, output_size=4, name="Simple CNN"):
		super().__init__()
		self.add(
			BatchNormalization(
				axis=1,
				input_shape=input_shape
			)
		)
		# Now we add to our model layer by layer
		self.add(
			BatchNormalization(

			)
		)

		self.add(
			Conv2D(
				filters=32,
				kernel_size=(3,3),
				strides=(1,1),
				padding="same",
				activation="relu"
			)
		)
		self.add(
			Conv2D(
				filters=32,
				kernel_size=(3,3),
				strides=(1,1),
				padding="same",
				activation="relu"
			)
		)

		self.add(
			MaxPooling2D(
				pool_size=(2,2),
				strides=None,
				padding="valid"
			)
		)
		self.add(
			Dropout(0.25)
		)
		# At ths point, each image has been converted to a shape of 13, 13, 32
		self.add(
			Conv2D(
				filters=64,
				kernel_size=(3,3),
				strides=(1,1),
				padding="same",
				activation="relu"
			)
		)

		self.add(
			MaxPooling2D(
				pool_size=(2,2),
				strides=None,
				padding="valid"
			)
		)

		self.add(
			Conv2D(
				filters=128,
				kernel_size=(3,3),
				strides=(1,1),
				padding="same",
				activation="relu"
			)
		)
		self.add(
			MaxPooling2D(
				pool_size=(2,2),
				strides=None,
				padding="valid"
			)
		)
		self.add(
			Dropout(0.25)
		)
		# 10, 10, 32
		self.add(Flatten())
		
		# We finish with two dense layers
		self.add(
			Dense(
				units=64,
				activation="relu",
				use_bias=True,
			)
		)
		self.add(
			Dropout(0.25)
		)

		# And the last layer to get an output of shape 10
		self.add(
			Dense(
				units=output_size,
				activation="softmax",
				use_bias=True
			)
		)

		self.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])

	def fit(self, X, Y):
		super().fit(
			x=X,
			y=Y,
			batch_size=64,
			epochs=20,
			verbose=1,
			validation_split=0.2,
			shuffle=True
		)
	
	def predict(self, X):
		# Get the prediction from the model
		result = super().predict(
			x=X
		)
		
		return result

def load_model(directory="model"):
	"""arch_path = os.path.join(directory, "architecture.json")
	with open(arch_path, 'r') as arch_file:
		json_string = arch_file.read()
	model = K.models.model_from_json(json_string, custom_objects={"SmallModel": SmallModel})"""
	cnn = SmallModel()
	weight_path = os.path.join(directory, "weights.h5")
	cnn.load_weights(weight_path)

	cnn.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])

	return cnn