import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D

model = Sequential([
    Conv2D(16, (3, 3), activation="relu", input_shape=(32, 32, 3)),
    MaxPooling2D((3, 3)),
    Flatten(),
    Dense(64, activation=f"relu"),
    Dense(10, activation="softmax")
])

print(model.summary())
