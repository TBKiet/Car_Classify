import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image
import os

# Thiết lập trang
st.set_page_config(
    page_title="Car Recognition App",
    page_icon="🚗",
    layout="centered"
)

# Tiêu đề và mô tả
st.title("🚗 Car Recognition App")
st.markdown("""
This app can recognize different types of cars:
- Sedan
- Sports Car
- SUV
- Truck
""")

# Load model
@st.cache_resource
def load_car_model():
    try:
        model = load_model('best_model.h5')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Hàm dự đoán
def predict_car(model, image):
    # Tiền xử lý ảnh
    img = Image.open(image)
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    
    # Dự đoán
    predictions = model.predict(img_array)
    
    # Lấy top 3 dự đoán
    top_3_idx = np.argsort(predictions[0])[-3:][::-1]
    top_3_probs = predictions[0][top_3_idx]
    
    # Map index to class names
    class_names = ['Sedan', 'Sports Car', 'SUV', 'Truck']
    results = [(class_names[idx], float(prob)) for idx, prob in zip(top_3_idx, top_3_probs)]
    
    return results

# Load model
model = load_car_model()

if model is not None:
    # Upload ảnh
    uploaded_file = st.file_uploader("Choose a car image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Hiển thị ảnh
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Nút dự đoán
        if st.button("Predict"):
            with st.spinner("Analyzing..."):
                # Dự đoán
                predictions = predict_car(model, uploaded_file)
                
                # Hiển thị kết quả
                st.subheader("Predictions:")
                
                # Tạo progress bars cho top 3 dự đoán
                for car_type, prob in predictions:
                    st.write(f"{car_type}: {prob:.2%}")
                    st.progress(float(prob))
                
                # Hiển thị kết quả tốt nhất
                best_prediction = predictions[0]
                st.success(f"Most likely: {best_prediction[0]} ({best_prediction[1]:.2%})")
                
                # Thêm thông tin về loại xe
                st.subheader("About the predicted car type:")
                car_info = {
                    'Sedan': "A sedan is a passenger car with a three-box configuration with separate compartments for engine, passenger, and cargo.",
                    'Sports Car': "A sports car is designed to emphasize handling, performance, and driving pleasure. They typically have a two-seat layout and are designed for spirited performance.",
                    'SUV': "A sport utility vehicle (SUV) is a car classification that combines elements of road-going passenger cars with features from off-road vehicles.",
                    'Truck': "A truck is a motor vehicle designed to transport cargo, carry specialized payloads, or perform other utilitarian work."
                }
                st.info(car_info[best_prediction[0]])

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and TensorFlow") 