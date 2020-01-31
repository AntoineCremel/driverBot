#!/usr/bin/python3.7

import numpy as np
import robotCode.motor
import model
import robotCode.camera as camera
import robotCode.motor as motor
import time
import image_load

def auto_drive(neural, past_influence=0.2):
    """
    Function to drive automatically using the image from the camera.
    """
    # Initialise the car components
    cam = camera.Camera()
    cam.camera_init()
    mot = motor.Motor()


    # Create a variable that represents the previous decision
    prev_average = np.aray([0, 0, 0, 0])
    # Then we enter a loop
    while True:
        start_time = time.time()
        image = cam.camera.get_image()
        label = neural.predict(image)

        # Now we produce an average of devision
        choice = (1-past_influence) * label + past_influence * prev_average
        # Convert our choice into a label
        label = image_load.cat_to_label(choice)
        if label == "F":
            pass
