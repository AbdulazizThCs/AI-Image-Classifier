# AI Image Classifier 

An AI-based image classification system that identifies images as Human, Robot, or Animal using a pre-trained TensorFlow model integrated via Python.

# Features
- Classifies images into: **Human**, **Robot**, **Animal**
- Pre-trained TensorFlow model (.h5)
- High-accuracy predictions
- Easily extendable with new classes
- Readable Python code structure

# How to Use

**1️- Create and Train the Model**  
Go to Teachable Machine, create a new Image Project, add your classes, and train the model using appropriate images.

**2️- Export the Trained Model**  
After training, export the model in **TensorFlow Keras** format. This will generate two essential files:
- `keras_model.h5`  
- `labels.txt`

**3️- SetUp Your Environment**  
Open **Google Colab** or any preferred Python editor, and install the tensorflow librare by running:

`!pip install tensorflow==2.12.1`

**4️- Upload Required Files**

Upload the following into your working directory:

- `keras_model.h5`
- `labels.txt`
- Test image files (`test1.jpg`, `test2.jpg`, `test3.jpg`)

**5️- Run the Prediction Script**

Use the provided script `predict_human_robot_animal.py`.

In the script, update the image path with the path to your test image.
Run the script to display the predicted class and confidence score.

<br>
<hr>

**Developed by Abdulaziz AL-Thomali**

