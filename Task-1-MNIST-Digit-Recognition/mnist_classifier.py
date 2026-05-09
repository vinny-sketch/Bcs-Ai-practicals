# Import required libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np

# Load MNIST dataset
# Requirement (a): Download and load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the neural network model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("\nModel Accuracy:", test_accuracy)

# Requirement (b): Distinguish digits 0-9
# Predict first 10 test images
predictions = model.predict(x_test[:10])

print("\nDigit Predictions:\n")

for i in range(10):
    predicted_digit = np.argmax(predictions[i])
    actual_digit = y_test[i]

    print(f"Image {i+1}:")
    print(f"Actual Digit    : {actual_digit}")
    print(f"Predicted Digit : {predicted_digit}")
    print("---------------------------")
