#!/usr/bin/python3.7

import keras as K
import model
import image_load
import numpy as np
from PIL import Image

# Test loading and prediction from the model
loaded_model = model.load_model()
loaded_model.summary()

# Load an image 
image = Image.open("lane_images/2020-01-15_07-42-22-472551.jpg")
image.show()
image = image.resize((64, 36))
image_list = np.array([list(image.getdata())])
image_list = image_load.format_X(image_list, [64, 36])
result = loaded_model.predict(image_list)

print("Result :", result)
