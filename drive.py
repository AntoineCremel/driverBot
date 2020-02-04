#!/usr/bin/python3.7

import numpy as np
import robotCode.motor
import model
import robotCode.camera as camera
import robotCode.motor as motor
import time
import image_load
import image_modification

def wait(start_time, frame_duration):
    end_time = time.time()
    elapsed = end_time - start_time()
    remaining = frame_duration - elapsed
    if remaining >= 0:
        time.sleep(remaining)

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
        # I/ La caméra prend une photo
        image = cam.camera.get_image()
        formatted = image_load.format_single_image(image)
        # II/ Conversion via le système de détection de lignes
        modified = image_modification.modify(formatted)
        # III/ La photo est envoyée au réseau de neurone de convolution
        label = neural.predict(modified)[0]

        # IV/ Mise à la moyenne mobile
        choice = (1-past_influence) * label + past_influence * prev_average
        # V/ Les roues s'activent en fonction de la direction déterminée
        label = image_load.cat_to_label(choice)
        if label == "F":
            mot.forward()
        elif label == "R":
            mot.right()
        elif label == "L":
            mot.left()
        elif label == "B":
            mot.backward()

        # Si le traitement a pris moins de temps que la durée prévue,
        wait(start_time, 1/frame_rate)
