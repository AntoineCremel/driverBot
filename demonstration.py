#!/usr/bin/python3.7

import model
import image_load
from os import path

cnn = model.load_model()

image_file_list = [
	"2020-01-15_07-47-08-653929.jpg",
	"2020-01-15_07-42-24-714051.jpg"
]


for file_name in image_file_list:
	completed_path = path.join("lane_images", file_name)
	image = image_load.format_one_file(completed_path, model.standard_format, show=True)

	prediction = cnn.predict(image)

	print("Result:", prediction)
	chosen = image_load.cat_to_label(prediction)
	print("Direction chosen:", chosen)

	user_input = input("(N)ext or e(X)it?")
	if user_input == "X":
		break