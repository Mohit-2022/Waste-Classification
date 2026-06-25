import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the trained model only once
model = load_model("garbage_classifier_Mobile.keras")

# IMPORTANT:
# The order MUST match train_generator.class_indices
CLASS_NAMES = [
    "Organic",
    "Textile",
    "battery",
    "glass",
    "metal",
    "paper",
    "plastic"
]


def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image


def predict_image(image):

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image, verbose=0)

    predicted_index = np.argmax(prediction)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(np.max(prediction) * 100)

    return predicted_class, confidence
