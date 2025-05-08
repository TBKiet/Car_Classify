import tensorflow as tf
import tensorflow_hub as hub

# Tải model MobileNetV2 từ TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
base_model = hub.load(model_url)

# Tạo model mới cho nhận diện xe
model = tf.keras.Sequential([
    # Input layer với kích thước 180x180x3
    tf.keras.layers.Input(shape=(180, 180, 3)),
    
    # Normalize pixels values
    tf.keras.layers.Rescaling(1./255),
    
    # Convolutional layers
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    
    # Flatten layer
    tf.keras.layers.Flatten(),
    
    # Dense layers
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # Thêm dropout để giảm overfitting
    tf.keras.layers.Dense(4, activation='softmax')  # 4 loại xe: sedan, suv, truck, sports_car
])

# Biên dịch model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# In ra summary của model để kiểm tra
model.summary()

# Lưu model
model.save('car_classification_model.keras')
print("\nModel đã được tạo và lưu thành công!") 