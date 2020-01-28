#!/usr/bin/python3.7

import keras as K
import model

# Test loading and prediction from the model
loaded_model = model.load_model()
loaded_model.summary()