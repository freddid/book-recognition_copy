from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os
from .model import predict_book
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('app/static/uploads', filename)
        file.save(file_path)
        
        # Предсказание книги
        book_id = predict_book(file_path)
        
        # Загрузка информации о книге из CSV
        df = pd.read_csv('data/main_dataset.csv')
        book_info = df[df['id'] == book_id].to_dict(orient='records')[0]
        
        return jsonify({"prediction": book_info['title']})
