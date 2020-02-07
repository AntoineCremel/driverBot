# Driver Bot project

This project aims to produce a system capable of driving a very simple prototype of an autonomous car. It uses Keras to build and train a neural network. Its inputs are the data collected by the sensors of the car, and its output is a command to the propulsion system of the car.

## User Manual

### Installation

Clone the repository

```
git clone https://github.com/AntoineCremel/driverBot.git
```

Create a virtual environment with python 3.7 using
```
python3.7 -m venv env
```

Enter the virtual environment
```
source env/bin/activate
```

Install the required libraries
```
pip3 install -r requirements.txt
```

You should be ready to machine learn

### Uses

Train the neural network and save it using train.py.

You can now use predict.py or demonstration.py to test your network.

labelisation.py is a script that you can use to add labels to any images that you might want to add to your training data.

## Characteristics

### Training data

The training images must all be placed in the lane_images directory alongside the labels.json file. Use exclusively the jpg format. The labels.json contains, for each image, the direction the car is expected to take if it sees that image.

### Neural network

The code related to the model is located in the model.py file. It contains a class that defines a specific architecture of convolutional neural network using the Keras Sequential API. If any change to that architecture or new architectures are to be defined, they should be written here.