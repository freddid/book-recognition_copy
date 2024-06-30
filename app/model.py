import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Загрузка модели
model = load_model('app/model/book_model.h5')

def predict_book(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    return predicted_class
