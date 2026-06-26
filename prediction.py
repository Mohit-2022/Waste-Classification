import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from ultralytics import YOLO

# ----------------------------
# Load Models
# ----------------------------

model = load_model("garbage_classifier_Mobile.keras")

# YOLO Object Detection Model
yolo_model = YOLO("yolov8n.pt")

# ----------------------------
# Class Names
# ----------------------------

CLASS_NAMES = [
    "Organic",
    "Textile",
    "battery",
    "glass",
    "metal",
    "paper",
    "plastic"
]

# ----------------------------
# Detect Object using YOLO
# ----------------------------

def detect_object(image):

    image_np = np.array(image)

    results = yolo_model(image_np, verbose=False)

    boxes = results[0].boxes

    if len(boxes) == 0:
        return image

    # Highest confidence object
    best_box = boxes[0]

    x1, y1, x2, y2 = best_box.xyxy[0].cpu().numpy()

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    cropped = image.crop((x1, y1, x2, y2))

    return cropped

# ----------------------------
# Preprocess Image
# ----------------------------

def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize((224,224))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image

# ----------------------------
# Prediction
# ----------------------------

def predict_image(image):

    # Detect object first
    detected_image = detect_object(image)

    processed_image = preprocess_image(detected_image)

    prediction = model.predict(processed_image, verbose=0)

    predicted_index = np.argmax(prediction)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(np.max(prediction) * 100)

    return predicted_class, confidence
