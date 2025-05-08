import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.header('CNN Model - Car Recognition')
car_names = ['sedan', 'suv', 'truck', 'sports_car']  # Thêm các loại xe bạn muốn nhận diện

model = load_model('car_classification_model.keras')  # Bạn cần train và lưu model mới

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array,0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    
    # Tạo danh sách kết quả cho tất cả các loại xe
    results = []
    for name, prob in zip(car_names, result):
        prob_percentage = np.round(prob * 100, 2)
        results.append(f"{name}: {prob_percentage}%")
    
    # Xác định loại xe có xác suất cao nhất
    max_prob_idx = np.argmax(result)
    max_prob = np.round(result[max_prob_idx] * 100, 2)
    predicted_car = car_names[max_prob_idx]
    
    return f"Dự đoán: {predicted_car} ({max_prob}%)\n\nPhân phối xác suất:\n" + "\n".join(results)

uploaded_file = st.file_uploader('Vui lòng tải lên hình ảnh xe')
if uploaded_file is not None:
    with open(os.path.join('Samples', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Hiển thị ảnh
    st.image(uploaded_file, width=200)
    
    # Hiển thị kết quả phân loại
    st.text(classify_images(uploaded_file)) 