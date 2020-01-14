#!/usr/bin/python3

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense

class SmallModel(Sequential):
	def __init__(self, input_shape=(28,28, 1)):
		super().__init__()

		# Now we add to our model layer by layer
		self.add(
			Conv2D(
				filters=16,
				kernel_size=(3,3),
				strides=(1,1),
				padding="valid",
				input_shape=input_shape
			)
		)

		self.add(
			MaxPooling2D(
				pool_size=(2,2),
				strides=None,
				padding="valid"
			)
		)
		# At ths point, each image has been converted to a shape of 13, 13, 16

		self.add(
			Conv2D(
				filters=32,
				kernel_size=(4,4),
				strides=(1,1),
				padding="valid",
				input_shape=input_shape
			)
		)
		# 10, 10, 32
		
		# We finish with two dense layers
		self.add(
			Dense(
				units=128,
				activation="relu",
				use_bias=True,
			)
		)

		# And the last layer to get an output of shape 10
		self.add(
			Dense(
				units=10,
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
			validation_split=0.05
		)