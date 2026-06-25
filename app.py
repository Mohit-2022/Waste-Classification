import streamlit as st
from PIL import Image

from prediction import predict_image
from waste_info import get_waste_info

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Smart Waste Classification",
    page_icon="♻️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("♻️ AI Smart Waste Classification System")

st.markdown("""
### Empowering Sustainable Waste Management Through Artificial Intelligence
Upload an image of waste and let AI identify its category while providing environmental awareness and recycling guidance.
""")

st.divider()

# -----------------------------
# Choose Input Method
# -----------------------------

st.subheader("Choose Input Method")

input_method = st.radio(
    "",
    ["📤 Upload Image", "📷 Take Photo"],
    horizontal=True
)

uploaded_file = None

if input_method == "📤 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

elif input_method == "📷 Take Photo":

    uploaded_file = st.camera_input("Take a Picture")

# -----------------------------
# If an image is available
# -----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Uploaded Image")

        st.image(image, use_container_width=True)

    with col2:

        predicted_class, confidence = predict_image(image)

        info = get_waste_info(predicted_class)

        st.subheader("Prediction")

        st.markdown(
            f"## {info['emoji']} **{predicted_class.upper()}**"
        )

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

        st.progress(confidence/100)

        st.markdown("---")

        st.subheader("💡 Did You Know?")

        st.info(info["fact"])

        st.subheader("🌱 What You Can Do")

        for tip in info["tips"]:

            st.write(f"✅ {tip}")

        st.markdown("---")

        st.subheader("♻ Recommended Disposal")

        st.success(info["bin"])

        st.subheader("Environmental Impact")

        st.warning(info["impact"])
