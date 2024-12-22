# -*- coding: utf-8 -*-
"""malaria deployment .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e0bcSUWS7YCz2yFg2hEwzwJ2GbnUl7HO
"""

import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('malaria_model.h5')  # تأكد من وجود الملف الصحيح

# Define the class labels
class_labels = {
    0: 'Infected',  # خلية مصابة
    1: 'Uninfected'  # خلية غير مصابة
}

# Streamlit app
st.title("Malaria Cell Image Classification with CNN")
st.markdown("Upload an image of a cell, and the model will predict whether it is infected with malaria or not.")

# File uploader
uploaded_file = st.file_uploader("Upload a Cell Image (JPG/PNG)", type=["jpg", "png", "jpeg"])

# If an image is uploaded
if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Add a button for prediction
    if st.button("Classify"):
        # Preprocess the image
        image = image.resize((150, 150))  # Resize to model's input size
        image = np.array(image) / 255.0  # Normalize the image
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make predictions
        predictions = model.predict(image)
        predicted_index = np.argmax(predictions)
        predicted_class = class_labels[predicted_index]
        confidence_scores = predictions[0]

        # Display results
        st.markdown("### Prediction Results")
        st.success(f"**Predicted Class**: {predicted_class}")

        # Display confidence scores
        st.markdown("### Confidence Scores")
        for index, score in enumerate(confidence_scores):
            st.write(f"- {class_labels[index]}: {score:.2%}")

        st.markdown("---")  # Divider for clarity
        st.markdown("### *Stay Healthy and Fight Malaria!*")