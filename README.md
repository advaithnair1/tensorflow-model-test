### Introduction
This repository contains a simple Convolutional Neural Network (CNN) implemented using TensorFlow and Keras. The network is designed for image classification tasks.

### Model Description
The CNN architecture consists of the following layers:

1. **Convolutional Layer:**  
   - Number of filters: 16
   - Filter size: (3, 3)
   - Activation function: ReLU
   - Input shape: (32, 32, 3) (RGB images of size 32x32)

2. **Max Pooling Layer:**  
   - Pool size: (3, 3)
   - Reduces the spatial dimensions of the feature map

3. **Flatten Layer:**  
   - Flattens the 3D feature maps into a 1D vector for input to fully connected layers

4. **Dense Layer (Fully Connected):**  
   - Number of neurons: 64
   - Activation function: ReLU
   - Connects all neurons from the previous layer

5. **Output Layer (Dense):**  
   - Number of neurons: 10 (for 10 classes in the dataset)
   - Activation function: Softmax
   - Produces probabilities for each class
