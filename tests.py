#!/usr/bin/python3.7

from tensorflow.keras.datasets import mnist
from model import SmallModel
import keras.utils

def test_with_mnist():
	(x_train, y_train), (x_test, y_test) = mnist.load_data()
	# Reshape the data
	x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
	x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
	x_train = x_train.astype('float32')
	x_test = x_test.astype('float32')
	x_train /= 255
	x_test /= 255

	y_train = keras.utils.to_categorical(y_train, 10)
	y_test = keras.utils.to_categorical(y_test, 10)

	print("x_train shape:", x_train.shape)
	print("y_train shape:", y_train.shape)

	# Create the model
	model = SmallModel(input_shape=(28,28, 1), output_size=10)

	model.fit(x_train, y_train)

	score = model.evaluate(x_test,y_test)
	print('Test loss:', score[0])
	print('Test accuracy:', score[1])

