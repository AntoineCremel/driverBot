#!/usr/bin/python3

from tensorflow.keras.datasets import mnist
from model import SmallModel
import keras.utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Reshape the data
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

print(x_train.shape)
print(type(x_train))

# Create the model
model = SmallModel(input_shape=(28,28, 1))

model.fit(x_train, y_train)

model.evaluate(x_test,y_test)