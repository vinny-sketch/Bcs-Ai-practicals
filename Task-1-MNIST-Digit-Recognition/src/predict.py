# Import libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load trained model
model = tf.keras.models.load_model('../model/mnist_model.h5')

# Load image
image_path = '../outputs/0.png'

img = Image.open(image_path).convert('L')

# Resize image to 28x28
img = img.resize((28, 28))

# Convert image to numpy array
img_array = np.array(img)

# Invert colors if needed
img_array = 255 - img_array

# Normalize pixel values
img_array = img_array / 255.0

# Reshape for model input
img_array = img_array.reshape(1, 28, 28)

# Predict digit
prediction = model.predict(img_array)

predicted_digit = np.argmax(prediction)

# Display image
plt.imshow(img_array[0], cmap='gray')
plt.title(f"Predicted Digit: {predicted_digit}")
plt.axis('off')
plt.show()

print(f"Predicted Digit: {predicted_digit}")
