# Import libraries
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation
np.set_printoptions(suppress=True)

# Custom DepthwiseConv2D to ignore 'groups' param
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)

# Load model
model = tf.keras.models.load_model(
    '/content/keras_model.h5',
    custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D},
    compile=False
)

# Load labels
class_names = open("labels.txt", "r").readlines()

# Create data array
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Load image
image = Image.open("/content/R_Test.jpg").convert("RGB")

# Resize image to 224x224
image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

# Convert image to numpy array
image_array = np.asarray(image)

# Normalize image to [-1, 1]
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Add image to data array
data[0] = normalized_image_array

# Define a prediction function to avoid retracing
@tf.function(reduce_retracing=True)
def predict_image(input_data):
    return model(input_data, training=False)

# Predict using the function
prediction = predict_image(data)
prediction = prediction.numpy()  # Convert Tensor to numpy array
index = np.argmax(prediction)

# Get class name and confidence
class_name = class_names[index]
confidence_score = prediction[0][index]

# Prediction result
print("\n- Predicted Class:", class_name[2:].strip())
print("- Prediction Confidence Score:", confidence_score)
