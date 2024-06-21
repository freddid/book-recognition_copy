import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Загрузка модели
model = load_model('app/model/book_recognition_model.h5')

def predict_book_cover(img_path):
    """
    Функция для предсказания на основе изображения обложки книги.
    
    Параметры:
    img_path (str): Путь к изображению обложки книги.
    
    Возвращает:
    float: Предсказанное значение (метка).
    """
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return prediction[0][0]
