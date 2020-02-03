#!/usr/bin/python3.7

import numpy as np
import robotCode.motor
import model
import robotCode.camera as camera
import robotCode.motor as motor
import time
import image_load

def auto_drive(neural, past_influence=0.2, frame_rate=10):
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
            mot.forward()
        elif label == "R":
            mot.right()
        elif label == "L":
            mot.left()
        elif label == "B":
            mot.backward()

        end_time = time.time()
        elapsed = end_time - start_time()
        frame_duration = 1/frame_rate
        remaining = frame_duration - elapsed
