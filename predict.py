#!/usr/bin/python3

import keras as K
import os

def load_model(directory="model"):
	arch_path = os.path.join(directory, "architecture.json")
	with open(arch_path, 'r') as arch_file:
		json_string = arch_file.read()
	model = K.models.model_from_json(json_string)
	weight_path = os.path.join(directory, "weights.h5")
	model.load_weights(weight_path)

	model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])

	return model

# Test loading and prediction from the model
model = load_model()
model.summary()